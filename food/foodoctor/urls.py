from django.urls import path

from .views import base_views, db_control, detail_views

app_name = 'foodoctor'

urlpatterns = [
    path('', base_views.index, name='index'),

    # json 으로 된 식당 정보를 DB에 추가하는 db_control.temp() 실행
    # 현재 .save() 하는 코드를 temp()에 넣진 않음
    path('import/', db_control.insert_restaurant_data, name='import'),
    path('korean_food/', detail_views.temp, name='korean_food'),
    path('chinese_food/', detail_views.temp, name='chinese_food'),
    path('japanese_food/', detail_views.temp, name='japanese_food'),
    path('cafe_food/', detail_views.temp, name='cafe_food'),
    path('asian_western_food/', detail_views.temp, name='asian_western_food'),
    path('fast_food/', detail_views.temp, name='fast_food'),
    path('bunsik_food/', detail_views.temp, name='bunsik_food'),
    path('meat_food/', detail_views.temp, name='meat_food'),
    path('etc_food/', detail_views.temp, name='etc_food'),
]
