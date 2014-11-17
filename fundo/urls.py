from django.conf.urls import patterns, url
from fundo.views import FundoListView

urlpatterns = patterns('',
                       url(r'^$', FundoListView.as_view(),
                           name='fundo'),
                       )
