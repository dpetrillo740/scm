from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
        url(r'^$', 'shopifyapp.views.login'),
        url(r'^authenticate/$', 'shopifyapp.views.authenticate'),
        url(r'^finalize/$', 'shopifyapp.views.finalize'),
        url(r'^logout/$', 'shopifyapp.views.logout'),
)
