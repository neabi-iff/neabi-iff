# -*- coding: utf-8 -*-
from django.test import TestCase
from model_mommy import mommy
from django.core.urlresolvers import reverse
from should_dsl import should


class TestViewDocumentoDetail(TestCase):

    def setUp(self):
        self.fundo1 = mommy.make_recipe('fundo.fundo', nome='Escravos1',
                                        biblioteca=u"Central")
        self.fundo2 = mommy.make_recipe('fundo.fundo', nome='Escravos2',
                                        biblioteca=u"Fundação")
        self.serie1 = mommy.make_recipe('fundo.serie', nome=u"Ação de Liberdade")
        self.serie2 = mommy.make_recipe('fundo.serie', nome=u"Ação de Liberdade 2")
        self.serie3 = mommy.make_recipe('fundo.serie', nome=u"Ação de Liberdade 3")
        self.documento1 = mommy.make_recipe('fundo.documento',
                                            codigo_referencia="abc",
                                            titulo="Meu Documento",
                                            serie=self.serie1,
                                            fundo=self.fundo1)
        self.documento2 = mommy.make_recipe('fundo.documento',
                                            codigo_referencia="def",
                                            titulo="Meu Documento2",
                                            serie=self.serie2,
                                            fundo=self.fundo1)

    def test_url_documento_detail(self):
        response = self.client.get(reverse('documento-detail', args=[self.fundo1.pk, self.serie1.pk, self.documento1.pk]))
        response.status_code | should | equal_to(200)

    def test_check_template_usado_seja_documento_detail_html(self):
        response = self.client.get(reverse('documento-detail', args=[self.fundo1.pk, self.serie1.pk, self.documento1.pk]))
        response.template_name | should | equal_to(['fundo/documento_detail.html'])

    def test_check_se_esta_fazendo_query_documento_por_fundo_e_serie(self):
        response1 = self.client.get(reverse('documento-detail', args=[self.fundo1.pk, self.serie1.pk, self.documento1.pk]))
        documento_in_context1 = response1.context['documento']
        documento_in_context1 | should | equal_to(self.documento1)

        response2 = self.client.get(reverse('documento-detail', args=[self.fundo1.pk, self.serie2.pk, self.documento2.pk]))
        documento_in_context2 = response2.context['documento']
        documento_in_context2 | should | equal_to(self.documento2)

    def test_check_se_os_dados_do_documento_aparecem_na_pagina(self):
        response = self.client.get(reverse('documento-detail', args=[self.fundo1.pk, self.serie1.pk, self.documento1.pk]))
        response.content | should | contain(unicode(self.documento1).encode('utf-8'))
        response.content | should | contain(self.documento1.nota_conservacao.encode('utf-8'))
