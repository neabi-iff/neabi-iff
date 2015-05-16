from django.contrib import admin
from .models import Neabi, Contato,Publicacoes

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id','email','telefone','facebook','twitter', 'google_plus','descricao')

@admin.register(Neabi)
class NeabiAdmin(admin.ModelAdmin):
    list_display = ('id','sobre')

@admin.register(Publicacoes)
class PublicacoesAdmin(admin.ModelAdmin):
    list_display = ('titulo','arquivo', 'descricao')
