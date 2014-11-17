from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Fundo, Serie


class FundoList(ListView):
    model = Fundo


class SerieList(ListView):
    model = Serie
