from __future__ import unicode_literals
from django.utils.timezone import now

from django.db import models

# Create your models here.
class person(models.Model):
    name = models.CharField(max_length=70)
    id_number = models.IntegerField()
    address = models.CharField(max_length=70)
    age = models.IntegerField()
    date_added = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.date_added = now()

        super(person,self).save(*args,**kwargs)
