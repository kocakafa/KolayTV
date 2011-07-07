from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
     (r'^admin/', include(admin.site.urls)),
    # (r'^$', 'index.views.index'),
#     (r'^profile/', include('profiles.urls')), 
     #(r'^videos/', include('events.urls')),
 #    url(r'^', include('social_auth.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^(?P<path>.*\.(?i)(css|js|jpg|jpeg|png|gif|ico|swf|html|htm))$', 
         'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)