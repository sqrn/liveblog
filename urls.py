from django.conf.urls.defaults import *
from liveblog.liveupdate.models import Update
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
    url(r'^$', include('liveblog.liveupdate.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^updates-after/(?P<id>\d+)/$', 'liveblog.liveupdate.views.updates_after'),
)

urlpatterns += staticfiles_urlpatterns()