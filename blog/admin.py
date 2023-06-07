from django.contrib import admin
from .models import Postagem,Categoria
# Register your models here.

@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
    list_display=('titulo','texto','data_criacao','imagem')


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display=('nome',)

