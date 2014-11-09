# -*- coding: utf-8 -*-
from model_mommy.recipe import Recipe, foreign_key
from .models import Fundo
from .models import Serie

fundo = Recipe(Fundo,
               nome="Fundo de Escravos",
               descricao="Fundos de escravos de campos",
               biblioteca=u"não sei o nome"
               )

serie = Recipe(Serie,
               nome=u"Ação de Liberdade",
               descricao=u"descrição da serie"
               )

#area_docente = Recipe(AreaDocente)

# local = Recipe(Local)

#professor = Recipe(Professor)
