from django.contrib import admin
from .models import Documento, Serie, Fundo

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('titulo','codigo_referencia','nota_conservacao','data','autor','condicao_acesso','nota_gerais',\
        'serie', 'arquivo')

@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    list_display = ('nome','fundo', 'descricao')

@admin.register(Fundo)
class FundoAdmin(admin.ModelAdmin):
    list_display = ('nome','biblioteca','imagem', 'descricao')