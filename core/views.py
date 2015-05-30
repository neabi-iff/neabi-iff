from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Neabi, Contato, Publicacoes, Fundo, Serie, Documento, Projeto
from watson.views import SearchView
from django.http import Http404



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


class FundoList(ListView):
    model = Fundo
    paginate_by = 10


class SerieList(ListView):
    model = Serie
    paginate_by = 10

    def get_queryset(self):
        return Serie.objects.filter(fundo__slug=self.kwargs['slug'])


class DocumentoList(ListView):
    model = Documento
    paginate_by = 10

    def get_queryset(self):
        return Documento.objects.filter(serie__slug=self.kwargs['slug'])


class Search(SearchView):

    """View that performs a search and returns the search results."""

    models = (Serie, Documento, Fundo)
    paginate_by = 10


class ProjetoList(ListView):
    model = Projeto
    paginate_by = 10


class FundoDetail(DetailView):
    model = Fundo

    def get_object(self):
        try:
            fundo = Fundo.objects.get(projeto__slug=self.kwargs['slug'])
        except:
            fundo = Fundo.objects.get(slug=self.kwargs['slug'])
        return fundo

class ProjetoDetail(DetailView):
    model = Projeto


class SerieDetail(DetailView):
    model = Serie

class DocumentoDetail(DetailView):
    model = Documento
