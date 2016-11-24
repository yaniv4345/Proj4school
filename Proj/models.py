from __future__ import unicode_literals
from django.utils.timezone import now

from django.db import models

class person(models.Model):
    name = models.CharField(max_length=70)
    id_number = models.IntegerField(max_length=9,unique=True)
    address = models.CharField(max_length=70)
    age = models.IntegerField()
    date_added = models.DateField(default=now())

    def __str__(self):
        return self.name
    # def get_by_id(self,num):
    #     return self.person(id_number=num)
    def save(self, *args, **kwargs):
        self.date_added = now()
        super(person,self).save(*args,**kwargs)
