# -*- coding: utf-8 -*-
from model_mommy.recipe import Recipe, foreign_key
from .models import Fundo

fundo = Recipe(Fundo,
               titulo="Fundo de Escravos",
               descricao="Fundos de escravos de campos",
               biblioteca=u"não sei o nome"
               )

#area_docente = Recipe(AreaDocente)

# local = Recipe(Local)

#professor = Recipe(Professor)
