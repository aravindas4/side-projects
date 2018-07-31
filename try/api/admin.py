from django.contrib import admin

# Register your models here.

from .models import Catalog, Company

admin.site.register(Catalog)
admin.site.register(Company)
