from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from core.views import Search
from filebrowser.sites import site

urlpatterns = [
    url(r'^', include('core.urls')),
    url(r'^noticias/', include('zinnia.urls', namespace='zinnia')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/tinymce/', include('tinymce.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^tinymce/zinnia/', include('zinnia_tinymce.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^pesquisar/', Search.as_view(), name='search_neabi'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)