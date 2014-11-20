# -*- coding: utf-8 -*-
from django.test import TestCase
from model_mommy import mommy
from django.core.urlresolvers import reverse
from should_dsl import should


class TestViewHome(TestCase):

    def setUp(self):
        self.fundo1 = mommy.make_recipe('fundo.fundo', nome='Escravos',
                                        biblioteca=u"não sei o nome")
        self.fundo2 = mommy.make_recipe('fundo.fundo', nome='Escravos2',
                                        biblioteca=u"também não sei")

    def test_homepage(self):
        response = self.client.get('/')
        response.status_code |should| equal_to(200)

    def test_template_usado_seja_home_page_html(self):
        response = self.client.get('/')
        response.template_name |should| equal_to(['core/home_page.html'])

    def test_check_se_contem_url_para_ver_os_fundos(self):
        response = self.client.get('/')
        fundos_url = reverse('fundo')
        fundos_url |should| be_into(response.content)
