from django.conf.urls import patterns, include, url
from settings import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('noticias.urls')),
    url(r'^', include('eventos.urls')),
    url(r'^tagging_autocomplete/', include('tagging_autocomplete.urls')),
    url('^pages/', include('django.contrib.flatpages.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns += staticfiles_urlpatterns()

if DEBUG:
    urlpatterns += patterns('',
                (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
                )