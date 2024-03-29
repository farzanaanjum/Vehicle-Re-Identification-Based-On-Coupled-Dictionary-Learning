# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-09 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0003_addvehicles'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateCrime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RTO_id', models.CharField(max_length=50)),
                ('Reg_no', models.CharField(max_length=50)),
                ('carbrand', models.CharField(max_length=60)),
                ('Ownername', models.CharField(max_length=60)),
                ('Licence', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('Acc_Address', models.CharField(max_length=100)),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('Incident', models.CharField(max_length=500)),
            ],
        ),
    ]
