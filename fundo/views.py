from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Fundo, Serie, Documento
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView


class FundoList(ListView):
    model = Fundo


class SerieList(ListView):
    model = Serie

    def get_queryset(self):
        self.fundo = get_object_or_404(Fundo, id=self.kwargs['pk_fundo'])
        return Serie.objects.filter(documento__fundo=self.fundo).distinct()

    def get_context_data(self, **kwargs):
        context = super(SerieList, self).get_context_data(**kwargs)
        context['fundo'] = self.fundo
        return context

class DocumentoList(ListView):
    model = Documento

    def get_queryset(self):
        self.fundo = get_object_or_404(Fundo, id=self.kwargs['pk_fundo'])
        self.serie = get_object_or_404(Serie, id=self.kwargs['pk_serie'])
        return Documento.objects.filter(fundo=self.fundo, serie=self.serie)

    def get_context_data(self, **kwargs):
        context = super(DocumentoList, self).get_context_data(**kwargs)
        context['fundo'] = self.fundo
        context['serie'] = self.serie
        return context

class DocumentoDetail(DetailView):
    pass