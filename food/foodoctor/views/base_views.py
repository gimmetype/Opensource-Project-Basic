import django.conf
from django.shortcuts import render

from ..models import Restaurant


def index(request):
    return render(request, 'foodoctor/index.html')


def temp():
    from decimal import Decimal
    from datetime import time
    _name = '아키아키'
    _category = '돼지고기구이'
    _rating = Decimal('4.59')
    _address = '충북 청주시 서원구 내수동로 130 1층'
    _tel_number = '010-8915-5455'
    _end_time = time(1, 0)
    _menu = ['고유한판세트', '생목갈비', '숙성삼겹', '생목살']
    _price = [39000, 30000, 13000, 13000]
    _menu_img_src = [
        'https://search.pstatic.net/common/?autoRotate=true&quality=95&type=f400_300&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20230201_64%2F1675249926049KElDz_JPEG%2F069E43E1-0EB9-4F6F-BBEA-1E00F91FB493.jpeg',
        'https://search.pstatic.net/common/?autoRotate=true&quality=95&type=f400_300&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20230426_122%2F1682483583104qEsf8_JPEG%2F1.jpg',
        'https://search.pstatic.net/common/?autoRotate=true&quality=95&type=f400_300&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20230201_66%2F1675249904307EQae4_JPEG%2FEAE32748-80ED-4CCA-A81E-F2CD756AD422.jpeg',
        'https://search.pstatic.net/common/?autoRotate=true&quality=95&type=f400_300&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20230201_258%2F1675249882218zmKiy_JPEG%2F4D430149-7D2F-4DC3-8CA0-B906CC7E4119.jpeg']

    menu_list = []
    for i in range(len(_menu)):
        menu_element = {'name': f'{_menu[i]}',
                        'price': _price[i],
                        'img_src': f'{_menu_img_src[i]}'
                        }
        menu_list.append(menu_element)

    rest = Restaurant()
    rest.name = _name
    rest.address = _address
    rest.tel_number = _tel_number
    rest.category = _category
    rest.menu = menu_list
    rest.rating = _rating
    rest.save()
