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
'''
def insert_restaurant_data(request):
    from decimal import Decimal
    from datetime import time
    import json

    path = 'C:/Users/clc26/Documents/store_data.json'
    with open(path, 'r', encoding='UTF8') as f:
        json_data = json.load(f)
    restaurant_data = json_data['매장정보']
    count = 0
    for i in range(len(restaurant_data)):
        count += 1
        each_restaurant_data = restaurant_data[i]
        price_list = each_restaurant_data['price']
        price_list = list((map(lambda e: type_casting(e.replace('원', '').replace(',', ''), int), price_list)))
        each_restaurant_data['price'] = price_list
        each_restaurant_data['star'] = Decimal(each_restaurant_data['star'].replace('/5', ''))

        _menu = each_restaurant_data['menu']
        _menu_img_src = each_restaurant_data['menu_image']
        menu_list = []
        for idx in range(len(_menu)):
            menu_element = {'name': f'{_menu[idx]}',
                            'price': price_list[idx],
                            'img_src': None if len(_menu_img_src) <= idx else _menu_img_src[idx]
                            }
            menu_list.append(menu_element)

        _kwd = each_restaurant_data['kwd']
        _kwd_count = each_restaurant_data['kwd_count']
        kwd_list = []
        for i in range(len(_kwd)):
            kwd_element = {
                'keyword': f'{_kwd[i]}',
                'kwd_count': int(_kwd_count[i])
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
        print(rest)

    print(count)
    return render(request, 'foodoctor/index.html')
