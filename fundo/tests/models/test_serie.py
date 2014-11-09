# -*- coding: utf-8 -*-
from django.test import TestCase
from model_mommy import mommy
from fundo.models import Serie


class TestModelSerie(TestCase):

    def setUp(self):
        self.serie = mommy.make_recipe('fundo.serie', nome='Fundo de Escravo')

    def test_verifica_se_a_serie_foi_criado(self):
        all_serie_in_database = Serie.objects.all()
        self.assertEquals(len(all_serie_in_database), 1)
        self.assertEquals(self.serie.nome, "Fundo de Escravo")

    def test_representacao_unicode_do_objeto(self):
        self.assertEqual(unicode(self.serie), 'Fundo de Escravo')

    def test_verbose_name_da_classe(self):
        verbose_name = Serie._meta.verbose_name
        self.assertEqual(verbose_name, u'Série')

    def test_verbose_name_plural_da_classe(self):
        verbose_name_plural = Serie._meta.verbose_name_plural
        self.assertEqual(verbose_name_plural, u'Séries')

    def test_verbose_name_do_campo_descricao(self):
        descricao = Serie._meta.get_field('descricao')
        self.assertEqual('Descrição', descricao.verbose_name)
