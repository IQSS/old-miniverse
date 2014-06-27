from django.conf.urls import patterns, include, url


urlpatterns = patterns('metadata.views',
    url(r'^review-map-links/$', 'view_review_map_links', name='view_review_map_links'),

    #url(r'^check-links/last_idx-(?P<last_idx>\d{1,9})/(?P<orig_cnt>\d{1,9})/$', 'make_link_check', name='make_link_check_with_idx'),

    url(r'^check-links/$', 'make_link_check', name='make_link_check'),
                                
)
