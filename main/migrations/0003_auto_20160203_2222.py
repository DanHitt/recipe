# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-03 22:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_recipe_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.URLField(blank=True, null=True),
        ),
    ]