from django.contrib import admin
from .models import Documento, Serie, Fundo, Pagina


class PaginaInline(admin.StackedInline):
    model = Pagina
    extra = 0


class DocumentoAdmin(admin.ModelAdmin):
    inlines = [PaginaInline]


class SerieAdmin(admin.ModelAdmin):
    pass


class FundoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Documento, DocumentoAdmin)
admin.site.register(Serie, SerieAdmin)
admin.site.register(Fundo, FundoAdmin)
