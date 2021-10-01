from django.contrib import admin

# Register your models here.
from .models import subscribe

class subscribe_date_time(admin.ModelAdmin):
    readonly_fields= ('date',)

admin.site.register(subscribe, subscribe_date_time)
