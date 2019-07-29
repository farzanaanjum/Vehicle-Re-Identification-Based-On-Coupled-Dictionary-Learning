# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class RTO(models.Model):
    emp_id = models.CharField(primary_key=True,max_length=50)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50,default="None")
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50,help_text="Minimum of 8 Characters")
    branch = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.emp_id+";"+self.name+";"+self.gender+";"+self.email+";"+self.password+";"+self.branch+";"+self.phone
