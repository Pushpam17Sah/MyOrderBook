from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Admin)
admin.site.register(models.Supplier)
admin.site.register(models.Item)