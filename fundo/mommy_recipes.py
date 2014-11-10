# -*- coding: utf-8 -*-
from model_mommy.recipe import Recipe, foreign_key
from .models import Fundo, Serie, Documento
import datetime

fundo = Recipe(Fundo,
               nome="Fundo de Escravos",
               descricao="Fundos de escravos de campos",
               biblioteca=u"não sei o nome"
               )

serie = Recipe(Serie,
               nome=u"Ação de Liberdade",
               descricao=u"descrição da serie"
               )

documento = Recipe(Documento,
                   codigo_referencia="abc",
                   titulo="Meu Documento",
                   data=datetime.date.today(),
                   dimensao_suporte="dimensao",
                   nivel_descricao="nivel descricao",
                   autor="autor",
                   ambito_conteudo="ambito",
                   condicao_acesso=u"codição",
                   nota_conservacao=u"nota de conservação",
                   nota_gerais="nota gerais",
                   slug="",
                   serie=foreign_key(serie),
                   fundo=foreign_key(fundo)
                   )
