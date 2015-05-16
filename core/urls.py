from django.conf.urls import patterns, url
from core.views import NeabiDetail, ContatoDetail, PublicacoesList, FundoList, \
 SerieList, DocumentoList

urlpatterns = patterns('',
                       url(r'^$', NeabiDetail.as_view(), name='neabi_detail'),
                       url(r'^contato/$', ContatoDetail.as_view(), name='contato_detail'),
                       url(r'^publicacoes/$', PublicacoesList.as_view(), name='publicacoes_list'),
                       url(r'^acervo/$', FundoList.as_view(), name='fundo_list'),
                       url(r'^acervo/(?P<slug>[-_\w]+)/serie/$', SerieList.as_view(),
                          name='serie-list'),
                       url(r'^acervo/(?P<slug_fundo>[-_\w]+)/serie/(?P<slug>[-_\w]+)/documento/$', DocumentoList.as_view(),
                          name='documento-list'),
                       )