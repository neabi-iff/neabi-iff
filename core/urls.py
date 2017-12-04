from django.conf.urls import url
from core.views import NeabiDetail, ContatoDetail, PublicacoesList, \
    FundoList, DocumentoList, ProjetoList, FundoDetail, ProjetoDetail,\
    DocumentoDetail, SearchProject, SearchSerie, SearchDocumento, \
    SearchAcervo

urlpatterns = [
    url(r'^$', NeabiDetail.as_view(), name='neabi_detail'),
    url(r'^contato/$', ContatoDetail.as_view(), name='contato_detail'),
    url(r'^publicacoes/$', PublicacoesList.as_view(), name='publicacoes_list'),

    # PROJETOS
    url(r'^neabi/projetos/$', ProjetoList.as_view(), name='projeto_list'),
    url(r'^neabi/projetos/(?P<slug>[-_\w]+)/acervo/(?P<slug_fundo>[-_\w]+)/$',
        ProjetoDetail.as_view(), name='projeto_detail'),
    url(r'^neabi/projetos/(?P<slug_projeto>[-_\w]+)/acervo/(?P<slug_fundo>[-_\w]+)/serie/(?P<slug>[-_\w]+)/documentos/$',
        DocumentoList.as_view(), name='documento-list'),
    url(r'^neabi/projetos/(?P<slug_projeto>[-_\w]+)/acervo/(?P<slug_fundo>[-_\w]+)/serie/(?P<slug_serie>[-_\w]+)/documentos/(?P<slug>[-_\w]+)/$',
        DocumentoDetail.as_view(), name='documento-detail'),

    # ACERVOS
    url(r'^neabi/acervos/$', FundoList.as_view(), name='fundo_list'),
    url(r'^neabi/acervos/(?P<slug>[-_\w]+)/series/$',
        FundoDetail.as_view(), name='fundo_detail'),
    url(r'^neabi/acervos/(?P<slug_fundo>[-_\w]+)/series/(?P<slug>[-_\w]+)/documentos/$',
        DocumentoList.as_view(), name='documento-list2'),
    url(r'^neabi/acervos/(?P<slug_fundo>[-_\w]+)/series/(?P<slug_serie>[-_\w]+)/documentos/(?P<slug>[-_\w]+)/$',
        DocumentoDetail.as_view(), name='documento-detail2'),

    #Ajax
    url(r'^ajax/search_project/$', SearchProject.as_view(), name='search_project'),
    url(r'^ajax/(?P<slug>[-_\w]+)/search_serie/$', SearchSerie.as_view(), name='search_serie'),
    url(r'^ajax/(?P<slug>[-_\w]+)/search_documento/$', SearchDocumento.as_view(), name='search_documento'),

    url(r'^ajax/search_acervo/$', SearchAcervo.as_view(), name='search_acervo'),
]
