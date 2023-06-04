import django.conf
from django.shortcuts import render

from ..models import Restaurant


'''
첫번째 인자 e : 형변환 대상 객체
두번째 인자 _type : casting 할 type

return 은 형변환된 객체를 반환
이때, 형변환에 실패하면 e를 그대로 반환한다

ex) type_casting('421', int) -> 421
type_casting('42~45', int) -> '42~45': str
'''


def type_casting(e, _type):
    try:
        e = _type(e)
    except ValueError:
        return e
    except TypeError:
        return e
    else:
        return e


'''
json 으로 식당 정보들을 받고
db에 추가

현재 json 파일에 대한 path 지정 필요

todo) 
json 경로 설정
'''


def insert_restaurant_data(request):
    import os
    import sys
    import urllib.request
    from decimal import Decimal
    import json

    path = 'C:/Users/clc26/store_data_modification_test.json'
    with open(path, 'r', encoding='UTF8') as f:
        json_data = json.load(f)
    restaurant_data = json_data['매장정보']
    count = 0
    for each_restaurant_data in restaurant_data:
        if len(Restaurant.objects.filter(name=each_restaurant_data['name'])) != 0:
            continue
        count += 1
        price_list = each_restaurant_data['price']
        price_list = list((map(lambda e: type_casting(e.replace('원', '').replace(',', ''), int), price_list)))
        each_restaurant_data['price'] = price_list
        each_restaurant_data['star'] = Decimal(each_restaurant_data['star'].replace('/5', ''))

        _menu = each_restaurant_data['menu']
        _menu_img_src = each_restaurant_data['menu_image']
        menu_list = []
        for idx in range(len(_menu)):
            if type(price_list[idx]) == int:
                menu_element = {'name': f'{_menu[idx]}',
                                'price': price_list[idx],
                                'price_str' : str(price_list[idx]),
                                'img_src': None if len(_menu_img_src) <= idx else _menu_img_src[idx]
                                }
            else:
                menu_element = {'name': f'{_menu[idx]}',
                                'price' : None,
                                'price_str': price_list[idx],
                                'img_src': None if len(_menu_img_src) <= idx else _menu_img_src[idx]
                                }
            menu_list.append(menu_element)

        _kwd = each_restaurant_data['kwd']
        _kwd_count = each_restaurant_data['kwd_count']
        kwd_list = []
        for k in range(len(_kwd)):
            kwd_element = {
                'text': f'{_kwd[k]}',
                'count': int(_kwd_count[k])
            }
            kwd_list.append(kwd_element)

        rest = Restaurant()
        rest.name = each_restaurant_data['name']
        rest.category = each_restaurant_data['tag_name']
        rest.tel_number = each_restaurant_data['tel']
        rest.rating = each_restaurant_data['star']
        rest.address = each_restaurant_data['addr']
        rest.menu = menu_list
        rest.keyword = kwd_list
        rest.save()

    print(count)
    return render(request, 'foodoctor/index.html')


def refactor_road_address_all(request):
    import re
    rest_list = Restaurant.objects.all()
    road_address_discriminant = re.compile(r"[가-힣]+길 |[가-힣]+로 ")
    si_re = re.compile(r"[가-힣]+시 ")
    gu_re = re.compile(r"[0-9가-힣]+구 ")
    road_re = re.compile(r"[0-9가-힣]+로([0-9]+번가*길)* [0-9]+(-[0-9]+)*")
    count = 0
    for each in rest_list:
        address = each.address
        if road_address_discriminant.search(address) is None:
            print(f'{address} 는 지번 주소입니다')
            continue
        else:
            # print(f'{address} 는 도로명 주소입니다')
            count += 1

        road_address = '충북 '
        match = si_re.search(address)
        if match is not None:
            road_address = road_address + match.group(0)
        match = gu_re.search(address)
        if match is not None:
            road_address = road_address + match.group(0)
        match = road_re.search(address)
        if match is not None:
            road_address = road_address + match.group(0)
        else:
            print("no road")

        # print(road_address)
        # save() 에서 에러 나서 도큐먼트 수정할때 쓸 save 폼을 만들어야함
        each.road_address = road_address
        each.save()

    print(count)
    return render(request, 'foodoctor/index.html')
