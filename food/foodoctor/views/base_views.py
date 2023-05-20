from django.shortcuts import render

from djongo import models

def index(request):
    return render(request, 'foodoctor/index.html')
