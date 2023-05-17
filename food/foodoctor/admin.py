from django.contrib import admin

from .modelExample import Author, Entry, SmallEntry

# Register your models here.
admin.site.register([Author, Entry])
admin.site.register(SmallEntry)