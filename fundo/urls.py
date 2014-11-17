from django.conf.urls import patterns, url
from fundo.views import FundoList, SerieList

urlpatterns = patterns('',
                       url(r'^$', FundoList.as_view(),
                           name='fundo'),
                       url(r'^(?P<pk>\d+)/serie/$', SerieList.as_view(),
                           name='serie-list'),
                       )
