# -*- coding: utf-8 -*-
from django.test import TestCase
from model_mommy import mommy
from fundo.models import Pagina
from fundo.mommy_recipes import documento


class TestModelPagina(TestCase):

    def setUp(self):
        self.pagina = mommy.make_recipe('fundo.pagina',
                                        arquivo="documento.jpg",
                                        documento=documento.make(titulo="My Documento",
                                                                 codigo_referencia="abc"
                                                                 )
                                        )

    def test_verifica_se_a_pagina_foi_criada(self):
        all_paginas_in_database = Pagina.objects.all()
        self.assertEquals(len(all_paginas_in_database), 1)
        self.assertEquals(self.pagina.arquivo, u"documento.jpg")
        self.assertEquals(unicode(self.pagina.documento), "My Documento (abc)")

    def test_representacao_unicode_do_objeto(self):
        self.assertEqual(unicode(self.pagina), u"documento.jpg (abc)")

    def test_verbose_name_da_classe(self):
        verbose_name = Pagina._meta.verbose_name
        self.assertEqual(verbose_name, 'Pagina')

    def test_verbose_name_plural_da_classe(self):
        verbose_name_plural = Pagina._meta.verbose_name_plural
        self.assertEqual(verbose_name_plural, 'Paginas')

    def test_upload_do_arquivo_para_a_pasta_paginas(self):
        arquivo = Pagina._meta.get_field('arquivo')
        self.assertEqual(arquivo.upload_to, 'paginas/')
