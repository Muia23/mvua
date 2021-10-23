from django.db import models

# Create your models here.
class Home(models.Model):
    dayname = models.CharField(max_length=100, blank=False)
    dayweatherlogo = models.URLField(max_length = 2000, blank=False)
    rainamount = models.CharField(max_length=100, blank=False)
    dayweathertext = models.CharField(max_length=100, blank=False)
    daytemp = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.dayname

    @classmethod
    def get_all(cls):
        home = cls.objects.all()
        return home