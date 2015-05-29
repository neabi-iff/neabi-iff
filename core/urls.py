from django.conf.urls import patterns, url
from core.views import NeabiDetail, ContatoDetail, PublicacoesList, FundoList, \
 SerieList, DocumentoList, ProjetoList, FundoDetail, ProjetoDetail

urlpatterns = patterns('',
    url(r'^$', NeabiDetail.as_view(), name='neabi_detail'),
    url(r'^contato/$', ContatoDetail.as_view(), name='contato_detail'),
    url(r'^publicacoes/$', PublicacoesList.as_view(), name='publicacoes_list'),
    url(r'^projeto/$', ProjetoList.as_view(), name='projeto_list'),
    url(r'^projeto/(?P<slug>[-_\w]+)/$', ProjetoDetail.as_view(), name='projeto_detail'),
    url(r'^projeto/(?P<slug>[-_\w]+)/acervo/$', FundoDetail.as_view(), name='fundo_detail'),
    url(r'^projeto/(?P<slug_projeto>[-_\w]+)/acervo/(?P<slug>[-_\w]+)/serie/$', SerieList.as_view(), name='serie-list'),
    url(r'^projeto/(?P<slug_projeto>[-_\w]+)/acervo/(?P<slug_fundo>[-_\w]+)/serie/(?P<slug>[-_\w]+)/documento/$', DocumentoList.as_view(), name='documento-list'),
    url(r'^acervos/$', FundoList.as_view(), name='fundo_list'),
    url(r'^acervos/(?P<slug>[-_\w]+)/serie/$', SerieList.as_view(), name='serie-list-2'),
    url(r'^acervos/(?P<slug_fundo>[-_\w]+)/serie/(?P<slug>[-_\w]+)/documento/$', DocumentoList.as_view(), name='documento-list2'),
)
