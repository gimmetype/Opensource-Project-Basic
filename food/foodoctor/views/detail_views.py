import django.conf
from django.shortcuts import render

from ..models import Restaurant


def detail(request, category: str):
    tag_names = {'korean': '한식',
                 'chinese': '중식',
                 'japanese': '돈까스/일식',
                 'dessert': '카페/디저트',
                 'asian': '아시안/양식',
                 'fastfood': '패스트푸트',
                 'bunsik': '분식',
                 'meat': '고기요리',
                 'etc': '기타'
                 }
    tag_names_to_title = {'korean': '한식',
                 'chinese': '중식',
                 'japanese': '돈까스·일식',
                 'dessert': '카페·디저트',
                 'asian': '아시안·양식',
                 'fastfood': '패스트푸드',
                 'bunsik': '분식',
                 'meat': '고기 요리',
                 'etc': '기타'
                 }
    restaurant_list = list(Restaurant.objects.filter(category=tag_names[category]))
    print(type(restaurant_list))
    context = {'restaurant_list': restaurant_list,
               'category': tag_names_to_title[category]
               }
    return render(request, 'foodoctor/detail.html', context)