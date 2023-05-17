from django.shortcuts import render

from ..modelExample import SmallEntry
from djongo import models

def index(request):
    return render(request, 'foodoctor/index.html')
