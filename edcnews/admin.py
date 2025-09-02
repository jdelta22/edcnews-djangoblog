from django.contrib import admin
from .models import Categoria, Noticia
# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    ...


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    ...
