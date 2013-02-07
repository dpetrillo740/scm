from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scmproj.views.home', name='home'),
    # url(r'^scmproj/', include('scmproj.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', include('shopifyapp.urls')),
    url(r'^', include('home.urls'), name='root_path'),
)
