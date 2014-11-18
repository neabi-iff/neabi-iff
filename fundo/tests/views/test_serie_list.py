# -*- coding: utf-8 -*-
from django.test import TestCase
from model_mommy import mommy
from model_mommy.recipe import foreign_key
from django.core.urlresolvers import reverse


class TestViewSerieList(TestCase):

    def setUp(self):
        self.fundo1 = mommy.make_recipe('fundo.fundo', nome='Escravos1',
                                        biblioteca=u"Central")
        self.fundo2 = mommy.make_recipe('fundo.fundo', nome='Escravos2',
                                        biblioteca=u"Fundação")
        self.serie1 = mommy.make_recipe('fundo.serie', nome=u"Ação de Liberdade")
        self.serie2 = mommy.make_recipe('fundo.serie', nome=u"Ação de Liberdade 2")
        self.documento1 = mommy.make_recipe('fundo.documento',
                                            codigo_referencia="abc",
                                            titulo="Meu Documento",
                                            serie=self.serie1,
                                            fundo=self.fundo1)
        self.documento2 = mommy.make_recipe('fundo.documento',
                                            codigo_referencia="def",
                                            titulo="Meu Documento2",
                                            serie=self.serie1,
                                            fundo=self.fundo1)

    def test_url_serie(self):
        response = self.client.get(reverse('serie-list', args=[self.fundo1.id]))
        self.assertEqual(response.status_code, 200)

    def test_check_template_usado_seja_serie_list_html(self):
        response = self.client.get(reverse('serie-list', args=[self.fundo1.id]))
        self.assertTemplateUsed(response, "fundo/serie_list.html")

    def test_check_se_esta_fazendo_query_serie_por_fundo(self):
        response1 = self.client.get(reverse('serie-list', args=[self.fundo1.pk]))
        series_in_context1 = response1.context['serie_list']
        self.assertEquals(list(series_in_context1), [self.serie1])

        response2 = self.client.get(reverse('serie-list', args=[self.fundo2.pk]))
        series_in_context2 = response2.context['serie_list']
        self.assertEquals(list(series_in_context2), [])

    def test_check_se_o_nome_das_series_aparecem_na_pagina(self):
        response = self.client.get(reverse('serie-list', args=[self.fundo1.pk]))
        self.assertIn(self.serie1.nome.encode('utf-8'), response.content)

    # def test_check_se_contem_url_para_ver_as_series_dos_fundos(self):
    #     response = self.client.get(reverse('fundo'))
    #     fundo1_series_list_url = reverse('serie-list', args=[self.fundo1.id])
    #     fundo2_series_list_url = reverse('serie-list', args=[self.fundo2.id])
    #     self.assertIn(fundo1_series_list_url, response.content)
    #     self.assertIn(fundo2_series_list_url, response.content)
