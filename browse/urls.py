from django.conf.urls.defaults import *

urlpatterns = patterns('browse.views',
    url(r'^spell/(?P<slug>[\w-]+)/$', 'spell_detail', name='spell_detail'),
)
