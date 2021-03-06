from django.conf.urls import patterns
from NDNScraper_interface import getPosts
from NDNScraper_interface import getIndividualPost

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns('',
        (r'^.*getPosts', getPosts),
        (r'^.*getPostContents/(.*)', getIndividualPost)  #anything after "getPostContents/" is the href parameter
    # Examples:
    # url(r'^$', 'django_code.views.home', name='home'),
    # url(r'^django_code/', include('django_code.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
