from django.urls import path

from .views import base_views, db_control

app_name = 'foodoctor'

urlpatterns = [
    path('', base_views.index, name='index'),

    # json 으로 된 식당 정보를 DB에 추가하는 db_control.temp() 실행
    # 현재 .save() 하는 코드를 temp()에 넣진 않음
    path('import/', db_control.temp, name='import')
]