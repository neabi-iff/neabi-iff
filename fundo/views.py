from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Fundo, Serie
from django.shortcuts import get_object_or_404


class FundoList(ListView):
    model = Fundo


class SerieList(ListView):
    model = Serie

    def get_queryset(self):
        self.fundo = get_object_or_404(Fundo, id=self.kwargs['pk'])
        return Serie.objects.filter(documento__fundo=self.fundo).distinct()
