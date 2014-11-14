from django.shortcuts import render
from django.views.generic.base import TemplateView
from fundo.models import Fundo


class HomePageView(TemplateView):
    template_name = "core/home_page.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['fundos'] = Fundo.objects.all()
        return context
