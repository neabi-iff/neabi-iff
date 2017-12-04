# -*- coding: utf-8 -*-
from .models import Neabi, Contato, Publicacoes, Fundo, Serie, \
    Documento, Projeto
from watson.views import SearchView
from django.http import Http404
from hamlpy.views.generic import DetailView, ListView, \
    HamlExtensionTemplateView
from django.views.generic.detail import SingleObjectMixin
from django.db.models import Q


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


# PROJETO


class ProjetoList(ListView):
    model = Projeto
    paginate_by = 10


class ProjetoDetail(SingleObjectMixin, ListView):
    paginate_by = 10
    template_name = "core/_detail.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Projeto.objects.all())
        return super(ProjetoDetail, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return self.object.fundo.serie_set.all()


# FUNDO


class FundoList(ListView):
    model = Fundo
    paginate_by = 10


class FundoDetail(SingleObjectMixin, ListView):
    paginate_by = 10
    template_name = "core/_detail.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fundo.objects.all())
        return super(FundoDetail, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return self.object.serie_set.all()


# DOCUMENTO

class DocumentoList(ListView):
    model = Documento
    paginate_by = 15

    def get_queryset(self):
        return Documento.objects.filter(serie__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(DocumentoList, self).get_context_data(**kwargs)
        context['serie'] = Serie.objects.get(slug=self.kwargs['slug'])
        return context


class DocumentoDetail(DetailView):
    model = Documento


class Search(HamlExtensionTemplateView, SearchView):
    models = (Serie, Documento, Fundo)
    paginate_by = 10


class SearchProject(ListView):
    template_name = "core/_search_project.html"
    model = Projeto

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            termo = request.GET.get('termo', None)
            self.queryset = Projeto.objects.filter(
                    Q(nome__icontains=termo) | Q(descricao__icontains=termo))
        return super(SearchProject, self).get(request, *args, **kwargs)


class SearchSerie(SingleObjectMixin, ListView):
    template_name = "core/_search_serie.html"
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fundo.objects.all())
        self.queryset = self.object.serie_set.all()
        if request.is_ajax():
            termo = request.GET.get('termo', None)
            self.queryset = self.object.serie_set.filter(
                Q(nome__icontains=termo) | Q(descricao__icontains=termo))
        return super(SearchSerie, self).get(request, *args, **kwargs)


class SearchDocumento(SingleObjectMixin, ListView):
    template_name = "core/_search_documento.html"
    paginate_by = 15

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Serie.objects.all())
        self.queryset = self.object.documento_set.all()
        if request.is_ajax():
            termo = request.GET.get('termo', None)
            self.queryset = self.object.documento_set.filter(
                Q(codigo_referencia__icontains=termo) |
                Q(titulo__icontains=termo) |
                Q(ano__icontains=termo) |
                Q(dimensao_suporte__icontains=termo) |
                Q(nivel_descricao__icontains=termo) |
                Q(ambito_conteudo__icontains=termo) |
                Q(autor__icontains=termo) |
                Q(condicao_acesso__icontains=termo) |
                Q(nota_conservacao__icontains=termo) |
                Q(nota_gerais__icontains=termo) |
                Q(nota_conservacao__icontains=termo)
                )
        return super(SearchDocumento, self).get(request, *args, **kwargs)


class SearchAcervo(ListView):
    template_name = "core/_search_acervo.html"
    model = Fundo

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            termo = request.GET.get('termo', None)
            self.queryset = Fundo.objects.filter(
                    Q(nome__icontains=termo) | Q(descricao__icontains=termo) |
                    Q(biblioteca__icontains=termo))
        return super(SearchAcervo, self).get(request, *args, **kwargs)
