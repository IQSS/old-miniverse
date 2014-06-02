from django.conf.urls import patterns, include, url


urlpatterns = patterns('mock_token.views_api',
    url(r'^singlefile/metadata/(?P<dv_token>\w{56})/?$', 'view_data_file_metadata', name="view_data_file_metadata"),

    url(r'^singlefile/metadata/$', 'view_data_file_metadata_base_url', name="view_data_file_metadata_base_url"),

    #url(r'^singlefile/file-content/(?P<dv_token>\w{32})/$', 'view_get_data_file', name='view_get_data_file'),

    #url(r'^geoconnect_map_it/(?P<data_file_md5>\w{32})/$', 'view_geoconnect_map_it', name='view_geoconnect_map_it'),


    #url(r'^choose2/(?P<shp_md5>\w{32})/(?P<shapefile_base_name>\w{3,90})/$', 'view_03_choose_shapefile_set', name="view_03_choose_shapefile_set"),

    #url(r'^view-shp/(?P<shp_md5>\w{32})/$', 'view_choose_shapefile', name="view_choose_shapefile"),
)
