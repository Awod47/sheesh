from django.contrib import admin

# Register your models here.
from .models import Product

class dateandtime(admin.ModelAdmin):
    readonly_fields= ('date',)

admin.site.register(Product, dateandtime)
