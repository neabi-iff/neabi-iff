# -*- coding: utf-8 -*-
from django.test import TestCase
from model_mommy import mommy

class TestViewHome(TestCase):

    def setUp(self):
        self.fundo1 = mommy.make_recipe('fundo.fundo', nome='Escravos',
                                       biblioteca=u"não sei o nome")
        self.fundo2 = mommy.make_recipe('fundo.fundo', nome='Escravos2',
                                       biblioteca=u"também não sei")

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

# http://www.tdd-django-tutorial.com/tutorial/3/
#     def test_template_usado_seja_home_page_html(self):
#         response = self.client.get('/')
#         self.assertTemplateUsed(response, "core/home_page.html")

    # def test_check_se_os_fundos_foi_passado_para_o_template(self):
    #     response = self.client.get('/')
    #     fundos_in_context = response.context['fundos']
    #     self.assertEquals(list(fundos_in_context),[self.fundo1,self.fundo2])



