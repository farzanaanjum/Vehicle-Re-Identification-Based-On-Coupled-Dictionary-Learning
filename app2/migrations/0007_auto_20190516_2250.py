# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-17 05:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0006_auto_20190511_0000'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AddVehicles',
        ),
        migrations.AddField(
            model_name='databse',
            name='otp',
            field=models.CharField(default=10.5, max_length=100),
            preserve_default=False,
        ),
    ]