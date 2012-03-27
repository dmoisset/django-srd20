from django.conf.urls.defaults import *

urlpatterns = patterns('favorites.views',
    url(r'^$', 'favorite_lists', name='favorite_lists'),
    url(r'^feat/(?P<slug>[\w-]+)/$', 'flag_as_favorite_feat', name='favorite_feat'),
    url(r'^feat/(?P<slug>[\w-]+)/delete/$', 'unfavorite_feat', name='unfavorite_feat'),
)
