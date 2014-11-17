# -*- coding: utf-8 -*-
from django.test import TestCase
from model_mommy import mommy
from django.core.urlresolvers import reverse


class TestViewFundoList(TestCase):

    def setUp(self):
        self.fundo1 = mommy.make_recipe('fundo.fundo', nome='Escravos',
                                        biblioteca=u"Central")
        self.fundo2 = mommy.make_recipe('fundo.fundo', nome='Escravos2',
                                        biblioteca=u"Fundação")

    def test_url_fundo(self):
        response = self.client.get(reverse('fundo'))
        self.assertEqual(response.status_code, 200)

    def test_check_template_usado_seja_fundo_list_html(self):
        response = self.client.get(reverse('fundo'))
        self.assertTemplateUsed(response, "fundo/fundo_list.html")

    def test_check_se_esta_passando_fundo_list(self):
        response = self.client.get(reverse('fundo'))
        fundos_in_context = response.context['fundo_list']
        self.assertEquals(list(fundos_in_context), [self.fundo1, self.fundo2])

    def test_check_se_o_nome_dos_fundos_aparecem_na_pagina(self):
        response = self.client.get(reverse('fundo'))
        self.assertIn(self.fundo1.nome, response.content)
        self.assertIn(self.fundo2.nome, response.content)

    def test_check_se_contem_url_para_ver_as_series_dos_fundos(self):
        response = self.client.get(reverse('fundo'))
        fundo1_series_list_url = reverse('serie-list', args=[self.fundo1.id])
        fundo2_series_list_url = reverse('serie-list', args=[self.fundo2.id])
        self.assertIn(fundo1_series_list_url, response.content)
        self.assertIn(fundo2_series_list_url, response.content)
