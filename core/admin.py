from django.contrib import admin
from core.models import Documento


class DocumentoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Documento, DocumentoAdmin)
