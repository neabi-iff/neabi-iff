from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Fundo, Serie, Documento
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView


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
