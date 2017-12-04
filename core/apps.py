# -*- coding: utf-8 -*-
from django.apps import AppConfig
from watson import search as watson


class CoreConfig(AppConfig):
    name = "core"
    verbose_name = u"Administração do Fundo"

    def ready(self):
        Fundo = self.get_model("Fundo")
        Serie = self.get_model("Serie")
        Documento = self.get_model("Documento")
        watson.register(Fundo)
        watson.register(Serie)
        watson.register(Documento)
