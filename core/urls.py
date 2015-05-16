from django.conf.urls import patterns, url
from core.views import NeabiDetail, ContatoDetail, PublicacoesList

urlpatterns = patterns('',
                       url(r'^$', NeabiDetail.as_view(),
                           name='neabi_detail'),
                       url(r'^contato/$', ContatoDetail.as_view(),
                           name='contato_detail'),
                       url(r'^publicacoes/$', PublicacoesList.as_view(),
                           name='publicacoes_list'),
                       # url(r'^(?P<slug>[-_\w]+)/serie/$', SerieList.as_view(),
                       #     name='serie-list'),
                       # url(r'^(?P<slug_fundo>[-_\w]+)/serie/(?P<slug>[-_\w]+)/documento/$', DocumentoList.as_view(),
                       #     name='documento-list'),
                       )