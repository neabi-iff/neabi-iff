# -*- coding: utf-8 -*-
from django.test import TestCase
from model_mommy import mommy
from fundo.models import Fundo


class TestModelFundo(TestCase):

    def setUp(self):
        self.fundo = mommy.make_recipe('fundo.fundo', titulo='Escravos',
                                       biblioteca=u"não sei o nome")

    def test_verifica_se_o_fundo_foi_criado(self):
        all_fundo_in_database = Fundo.objects.all()
        self.assertEquals(len(all_fundo_in_database), 1)
        self.assertEquals(self.fundo.titulo, "Escravos")
        self.assertEquals(self.fundo.biblioteca, u"não sei o nome")

    def test_representacao_unicode_do_objeto(self):
        self.assertEqual(unicode(self.fundo), 'Escravos')

    def test_verbose_name_da_classe(self):
        verbose_name = Fundo._meta.verbose_name
        self.assertEqual(verbose_name, 'Fundo')

    def test_verbose_name_plural_da_classe(self):
        verbose_name_plural = Fundo._meta.verbose_name_plural
        self.assertEqual(verbose_name_plural, 'Fundos')
