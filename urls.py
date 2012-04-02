from django.conf.urls.defaults import *
import browse.urls
import search.search_site

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^browse/', include(browse.urls)),
    (r'^$', 'search.views.search_start'),
    (r'^search/', include(search.search_site.urls)),
    (r'^account/', include('registration.backends.simple.urls')),
    (r"^likes/", include("phileo.urls")),
)
