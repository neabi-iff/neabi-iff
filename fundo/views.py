from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Fundo


class FundoListView(ListView):
    model = Fundo
