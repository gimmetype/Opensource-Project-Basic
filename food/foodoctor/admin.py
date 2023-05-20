from django.contrib import admin

from .modelExample import Author, Entry

# Register your models here.
admin.site.register([Author, Entry])