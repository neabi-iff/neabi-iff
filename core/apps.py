# -*- coding: utf-8 -*-
from django.apps import AppConfig
from watson import search as watson


class CoreConfig(AppConfig):
    name = "core"
    verbose_name = u"Administração do Fundo"

    def ready(self):
        fundo = self.get_model("Fundo")
        serie = self.get_model("Serie")
        documento = self.get_model("Documento")
        watson.register(fundo)
        watson.register(serie)
        watson.register(documento)
