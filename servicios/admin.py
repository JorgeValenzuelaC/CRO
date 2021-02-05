from django.contrib import admin
from .models import servicio
# Register your models here.

class Serivicoadmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

admin.site.register(servicio, Serivicoadmin)