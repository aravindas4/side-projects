# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length =100, blank = False)
    # phone_regex = RegexValidator(regex=r'^\0?\d{4}\-\d{6}$', message="Phone number must be entered in the format: '07777-777777'.  11 digits allowed.")
    phone_number = models.CharField(max_length=12, blank=True)
    '''user = models.ForeignKey(
        'User', related_name = 'companies',
        on_delete=models.CASCADE,
    )'''
    users = models.ManyToManyField('auth.User', related_name='companys')
    class Meta:
        ordering = ['-name']
    def __unicode__(self):
        return self.name

class Catalog(models.Model):
    name = models.CharField(max_length =100, blank = False)
    no_of_pcs = models.IntegerField(blank=True, default = 0)
    per_pcs_price = models.DecimalField(max_digits=6, decimal_places=2)
    company = models.ForeignKey(
        'Company',related_name = 'catalogs',
        on_delete=models.CASCADE,
    )
    def __unicode__(self):
        return self.name

# class WBUsers(User):
#     company = models.ForeignKey(
#         'Company', related_name = 'users',
#             on_delete=models.CASCADE,
#     )
