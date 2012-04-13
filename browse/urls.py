from django.conf.urls.defaults import *

urlpatterns = patterns('browse.views',
    url(r'^spell/(?P<slug>[\w-]+)/$', 'spell_detail', name='spell_detail'),
    url(r'^feat/(?P<slug>[\w-]+)/$', 'feat_detail', name='feat_detail'),
    url(r'^monster/(?P<slug>[\w-]+)/$', 'monster_detail', name='monster_detail'),

    url(r'^favorites/$', 'favorites', name='favorite_lists'),

)
