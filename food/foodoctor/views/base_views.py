import django.conf
from django.shortcuts import render

from ..models import Restaurant


def index(request):
    return render(request, 'foodoctor/index.html')
