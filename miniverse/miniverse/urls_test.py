from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api
from dataset.api import DatasetResource

v1_api = Api(api_name='v1')
v1_api.register(DatasetResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'miniverse.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^dataset/', include('dataset.urls')),
    
    url(r'^metadata/', include('metadata.urls')),

    url(r'^geo-api/', include('mock_token.urls')),

    url(r'^miniverse-admin/', include(admin.site.urls)),
    
    url(r'^api/', include(v1_api.urls)),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
