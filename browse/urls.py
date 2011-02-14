from django.conf.urls.defaults import *

urlpatterns = patterns('browse.views',
    url(r'^spell/(?P<id>\d+)/$', 'spell_detail', name='spell_detail'),
    url(r'^feat-type/(?P<id>\d+)/$', 'feat_type_detail', name='feat_type_detail'),
    url(r'^feat/(?P<id>\d+)/$', 'feat_detail', name='feat_detail'),
)
