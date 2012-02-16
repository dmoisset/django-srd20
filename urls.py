from django.conf.urls.defaults import *
import browse.urls

from django.contrib import admin
admin.autodiscover()
import search.search

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^browse/', include(browse.urls)),
    (r'^$', 'search.views.search_start'),
    (r'^search/', include(search.search.urls)),
)
