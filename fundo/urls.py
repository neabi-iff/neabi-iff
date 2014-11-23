from django.conf.urls import patterns, url
from fundo.views import FundoList, SerieList, DocumentoList, \
    DocumentoDetail

urlpatterns = patterns('',
                       url(r'^$', FundoList.as_view(),
                           name='fundo'),
                       url(r'^(?P<pk_fundo>\d+)/$', SerieList.as_view(),
                           name='serie-list'),
                       url(r'^(?P<pk_fundo>\d+)/serie/(?P<pk_serie>\d+)/$', DocumentoList.as_view(),
                           name='documento-list'),
                       url(r'^(?P<pk_fundo>\d+)/serie/(?P<pk_serie>\d+)/documento/(?P<pk>\d+)/$',
                           DocumentoDetail.as_view(), name='documento-detail'),
                       )
