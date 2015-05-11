from django.contrib import admin
from .models import Documento, Serie, Fundo, Arquivo

class ArquivoInline(admin.StackedInline):
    model = Arquivo


class DocumentoAdmin(admin.ModelAdmin):
    inlines = [ArquivoInline]


admin.site.register(Documento, DocumentoAdmin)
admin.site.register(Serie)
admin.site.register(Fundo)
