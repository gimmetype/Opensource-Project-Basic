# from django.db import models
from djongo import models

# Create your models here.


class Menu(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    price_str = models.TextField()
    img_src = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class BusinessHours(models.Model):
    open_time = models.TimeField()
    end_time = models.TimeField()
    breaktime_start = models.TimeField()
    breaktime_end = models.TimeField()
    holiday = models.JSONField()

    class Meta:
        abstract = True


class Keyword(models.Model):
    text = models.TextField()
    count = models.IntegerField()

    class Meta:
        abstract = True


class Restaurant(models.Model):
    _id = models.ObjectIdField()
    name = models.TextField()
    address = models.TextField()
    tel_number = models.TextField()
    business_hours = models.EmbeddedField(
        model_container=BusinessHours,
        null=True,
    )
    mapx = models.IntegerField()
    mapy = models.IntegerField()
    category = models.TextField()
    menu = models.ArrayField(
        model_container=Menu,
    )
    keyword = models.ArrayField(
        model_container=Keyword,
        null=True
    )
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    last_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
