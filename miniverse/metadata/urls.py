from django.conf.urls import patterns, include, url


urlpatterns = patterns('metadata.views',
    url(r'^review-map-links/$', 'view_review_map_links', name="view_review_map_links"),

)
