from django.db import models
from datetime import date

# Create your models here.
class Home(models.Model):
    date = models.DateField(auto_now_add=False, auto_now=False, blank=False)
    dayweatherlogo = models.URLField(max_length = 2000, blank=False)
    rainamount = models.CharField(max_length=100, blank=False)
    dayweathertext = models.CharField(max_length=100, blank=False)
    daytemp = models.CharField(max_length=100, blank=False)
    dayhumidity = models.CharField(max_length=100, blank=False)


    def __str__(self):
        return self.rainamount

    @classmethod
    def get_all(cls):
        home = cls.objects.all()
        return home

class RainData(models.Model):
    dayname = models.CharField(max_length=100, blank=False)
    rainamt = models.IntegerField(blank=False)

    def __str__(self):
        return self.dayname

    @classmethod
    def get_rainData(cls):
        data = cls.objects.all()
        return data