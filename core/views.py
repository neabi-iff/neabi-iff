from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from fundo.models import Fundo
from core.models import Contato, Acervo, SobreNeabi


class HomePageView(TemplateView):
    template_name = "core/home_page.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['fundos'] = Fundo.objects.all()
        return context


class Contato(ListView):
    model = Contato
    template_name = "core/contato_list.html"


class Acervo(ListView):
    model = Acervo
    template_name = "core/acervo_list.html"


class SobreNeabi(ListView):
    model = SobreNeabi
    template_name = "core/sobre_neabi_list.html"
