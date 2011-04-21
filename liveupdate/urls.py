from django.conf.urls.defaults import *
from liveblog.liveupdate.models import Update

from django.contrib import admin
admin.autodiscover()

 
urlpatterns = patterns('',   
    url(r'^$', 'django.views.generic.list_detail.object_list', {
        'queryset': Update.objects.all()
    }),


)