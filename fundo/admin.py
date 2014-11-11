from django.contrib import admin
from .models import Documento, Serie, Fundo


class DocumentoAdmin(admin.ModelAdmin):
    pass


class SerieAdmin(admin.ModelAdmin):
    pass


class FundoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Documento, DocumentoAdmin)
admin.site.register(Serie, SerieAdmin)
admin.site.register(Fundo, FundoAdmin)
