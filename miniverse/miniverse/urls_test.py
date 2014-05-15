from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'miniverse.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^dataset/', include('dataset.urls')),

    url(r'^geo-api/', include('mock_token.urls')),

    url(r'^miniverse-admin/', include(admin.site.urls)),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
