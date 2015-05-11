from django.conf.urls import patterns, url
from fundo.views import FundoList, SerieList, DocumentoList

urlpatterns = patterns('',
                       url(r'^$', FundoList.as_view(),
                           name='fundo_list'),
                       url(r'^(?P<slug>[-_\w]+)/serie/$', SerieList.as_view(),
                           name='serie-list'),
                       url(r'^(?P<slug_fundo>[-_\w]+)/serie/(?P<slug>[-_\w]+)/documento/$', DocumentoList.as_view(),
                           name='documento-list'),
                       )