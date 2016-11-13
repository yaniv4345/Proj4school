from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.
class person(models.Model):
    name = models.CharField(max_length=70)
    id_number = models.IntegerField()
    address = models.CharField(max_length=70)
    age = models.IntegerField()
    data_added = models.DateField(auto_now_add=True, blank=True)
