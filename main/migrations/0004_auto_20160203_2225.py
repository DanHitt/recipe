# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-03 22:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20160203_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='directions',
            field=models.TextField(blank=True, null=True),
        ),
    ]
