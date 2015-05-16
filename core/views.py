from django.views.generic.detail import DetailView
from django.views.generic import ListView
from core.models import Neabi, Contato, Publicacoes

class NeabiDetail(DetailView):
    model = Neabi

    def get_object(self):
        try:
            return Neabi.objects.first()
        except Neabi.DoesNotExist:
            raise Http404

class ContatoDetail(DetailView):
    model = Contato

    def get_object(self):
        try:
            return Contato.objects.first()
        except Contato.DoesNotExist:
            raise Http404

class PublicacoesList(ListView):
    model = Publicacoes
    paginate_by = 10
