import django.conf
from django.shortcuts import render

from ..models import Restaurant


def temp(request):
    return render(request, 'foodoctor/korean_restaurants.html')