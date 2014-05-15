from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'miniverse.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^dataset/', include('dataset.urls')),

    url(r'^miniverse-admin/', include(admin.site.urls)),

    url(r'^admin/', include(admin.site.urls)),
)
