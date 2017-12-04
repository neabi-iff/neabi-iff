from django.contrib import admin
from .models import Neabi, Contato, Publicacoes, Documento, Serie, Fundo, Social, Patrocinador, Projeto

from watson.admin import SearchAdmin

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id','email','telefone','facebook','twitter', 'google_plus','descricao')


@admin.register(Neabi)
class NeabiAdmin(admin.ModelAdmin):
    list_display = ('id','sobre')


@admin.register(Publicacoes)
class PublicacoesAdmin(admin.ModelAdmin):
    list_display = ('titulo','arquivo', 'descricao')


@admin.register(Documento)
class DocumentoAdmin(SearchAdmin):
    list_display = ('titulo','codigo_referencia','nota_conservacao','data','autor','condicao_acesso','nota_gerais',\
        'serie', 'arquivo')
    search_fields = ("titulo", "codigo_referencia",)


@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    list_display = ('nome','fundo', 'descricao')


@admin.register(Fundo)
class FundoAdmin(admin.ModelAdmin):
    list_display = ('nome','biblioteca','imagem', 'destaque','descricao', 'projeto')


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('id','facebook','twitter', 'google_plus')


@admin.register(Patrocinador)
class PatrocinadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'link', 'imagem')


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')

