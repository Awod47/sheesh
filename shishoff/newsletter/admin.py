from django.contrib import admin

# Register your models here.
from .models import Newsletter

class newsletter_time(admin.ModelAdmin):
    readonly_fields= ('date',)

admin.site.register(Newsletter, newsletter_time)