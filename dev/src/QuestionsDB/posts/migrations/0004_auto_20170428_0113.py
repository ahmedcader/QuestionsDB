# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 01:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_slug_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug_field',
            field=models.SlugField(auto_created=True, blank=True, null=True),
        ),
    ]