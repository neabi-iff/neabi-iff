# -*- coding: utf-8 -*-
from django.test import TestCase

class TestViewHome(TestCase):

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)