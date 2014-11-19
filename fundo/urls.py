from django.conf.urls import patterns, url
from fundo.views import FundoList, SerieList, DocumentoList

urlpatterns = patterns('',
                       url(r'^$', FundoList.as_view(),
                           name='fundo'),
                       url(r'^(?P<pk>\d+)/serie/$', SerieList.as_view(),
                           name='serie-list'),
                       url(r'^(?P<pk_fundo>\d+)/serie/(?P<pk_serie>\d+)$', DocumentoList.as_view(),
                        name='documento-list'),
                          )
