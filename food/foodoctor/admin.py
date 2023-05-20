from django.contrib import admin

from .modelExample import Author, Entry
from .models import Restaurant

# Register your models here.
admin.site.register([Author, Entry])
admin.site.register(Restaurant)
