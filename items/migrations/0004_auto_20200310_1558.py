# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-10 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_auto_20200303_1924'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='choices',
            new_name='sizes',
        ),
        migrations.AddField(
            model_name='item',
            name='categories',
            field=models.CharField(choices=[('w', 'Women Clothes'), ('m', 'Men Clothes'), ('k', 'Kids Clothes')], default='w', max_length=15),
        ),
    ]
