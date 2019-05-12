from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(null = False, unique = True, max_length = 50)
    description = models.CharField(null = False, max_length = 100)
    max_price = models.FloatField(null = False)
    min_price = models.FloatField(null = False)
