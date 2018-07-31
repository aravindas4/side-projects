# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-28 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excalci', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expense',
            options={'ordering': ('-expense_created',)},
        ),
        migrations.AddField(
            model_name='expense',
            name='expense_neccessity_flag',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='expense',
            name='expense_slug',
            field=models.SlugField(max_length=250, null=True, unique_for_date='expense_created'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='expense_name',
            field=models.CharField(max_length=200),
        ),
    ]