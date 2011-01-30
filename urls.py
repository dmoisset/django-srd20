from django.conf.urls.defaults import *
import browse.urls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^django_srd20/', include('django_srd20.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^browse/', include(browse.urls)),
    (r'^$', 'search.views.search_start'),
    (r'^search/$', 'search.views.search_results'),
)
