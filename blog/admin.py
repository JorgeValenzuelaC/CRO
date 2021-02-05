from django.contrib import admin
from .models import Categoria, Post


# Register your models here.

class categoriaAdmin(admin.ModelAdmin):
    readonly_fields=('fecha_creacion','fecha_actualizacion')

class postAdmin(admin.ModelAdmin):
    readonly_fields=('fecha_creacion','fecha_actualizacion')


admin.site.register(Categoria, categoriaAdmin)
admin.site.register(Post, postAdmin)