from django.conf.urls import patterns, include, url


urlpatterns = patterns('dataset.views',
    url(r'^list/$', 'view_dataset_list', name="view_dataset_list"),

    url(r'^map_it/(?P<data_file_md5>\w{32})/$', 'view_map_it', name='view_map_it'),

    url(r'^geoconnect_map_it/(?P<data_file_md5>\w{32})/$', 'view_geoconnect_map_it', name='view_geoconnect_map_it'),


    #url(r'^choose2/(?P<shp_md5>\w{32})/(?P<shapefile_base_name>\w{3,90})/$', 'view_03_choose_shapefile_set', name="view_03_choose_shapefile_set"),

    #url(r'^view-shp/(?P<shp_md5>\w{32})/$', 'view_choose_shapefile', name="view_choose_shapefile"),
)
