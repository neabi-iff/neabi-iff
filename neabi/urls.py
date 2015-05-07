from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from core.views import HomePageView
from core.views import Contato, Acervo, SobreNeabi

urlpatterns = patterns('',
    url(r'^', include('zinnia.urls', namespace = 'zinnia')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^tinymce/zinnia/', include('zinnia_tinymce.urls')),


    url(r'^fundo/', include('fundo.urls')),
    url(r'^contato/$', Contato.as_view(), name='contato'),
    url(r'^acervo/$', Acervo.as_view(), name='acervo'),
    url(r'^neabi/sobre/$', SobreNeabi.as_view(), name='sobre_neabi'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)