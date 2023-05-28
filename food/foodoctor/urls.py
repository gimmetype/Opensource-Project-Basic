from django.urls import path

from .views import base_views, db_control, detail_views

app_name = 'foodoctor'

urlpatterns = [
    path('', base_views.index, name='index'),

    # json 으로 된 식당 정보를 DB에 추가하는 db_control.temp() 실행
    # 현재 .save() 하는 코드를 temp()에 넣진 않음
    path('import/', db_control.insert_restaurant_data, name='import'),

    path('<str:category>/', detail_views.detail, name='detail')
]
'''
path('<chinese_food>/', detail_views.detail, name='chinese_food'),
path('japanese_food/', detail_views.detail, name='japanese_food'),
path('cafe_food/', detail_views.detail, name='cafe_food'),
path('asian_western_food/', detail_views.detail, name='asian_western_food'),
path('fast_food/', detail_views.detail, name='fast_food'),
path('bunsik_food/', detail_views.detail, name='bunsik_food'),
path('meat_food/', detail_views.detail, name='meat_food'),
path('etc_food/', detail_views.detail, name='etc_food'),
'''
