import os

from django.shortcuts import render
from django.shortcuts import render_to_response

from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from dataset.models import Dataset, DataFile
from dataset.mapit_metadata_helper import MetadataHelper
from metadata.models import GeographicMetadata

from mock_token.models import DataverseToken, ApplicationInfo

import json
from django.http import Http404

import logging
logger = logging.getLogger(__name__)

@login_required
def view_dataset_list(request):

    d = { 'page_title' : 'Dataset list' }
    
    # Pull geographic metadata and place in dict { dataset id : GeographicMetadata }
    #
    geo_metadata = GeographicMetadata.objects.filter(links_working=True).select_related('datafile__dataset').all()
    gm_dict = {}
    for gm in geo_metadata:
        gm_dict.setdefault(gm.datafile.id, []).append(gm)
    
    # Pull datasets and attach geographic metadata, if available
    #
    datasets = Dataset.objects.select_related('dataverse').all()
    datasets_updated = list(datasets)
    #for da in datasets:
    #    da.geo_metadata_list = gm_dict.get(da.id, None)
    #    datasets_updated.append(da)
    
    # Temp while figuring out steps
    d['datasets'] =  datasets_updated
    d['file_count'] = DataFile.objects.all().count()
    d['gis_file_count'] = DataFile.objects.filter(has_gis_data=True).count()

    return render_to_response('view_dataset_list.html', d\
                                , context_instance=RequestContext(request))


@login_required
def view_geoconnect_map_it(request, data_file_md5):
    """Create a DataverseToken and send it to GeoConnect
    """
    if not request.user.is_authenticated():
        return HttpResponse('Please log in to use the "Map It" link')
    try: 
        sf = DataFile.objects.select_related('dataset').get(md5=data_file_md5)
    except DataFile.DoesNotExist:
        return Http404('file not found for: %s' % data_file_md5)

    app_info = ApplicationInfo.objects.get(name='GeoConnect Harvard')
    
    # Does the user have an existing token?
    tokens = DataverseToken.objects.filter(application=app_info\
                                            , dataverse_user=request.user\
                                            , data_file=sf)
    
    # Are any of these tokens active?                
    tokens = [t for t in tokens if not t.has_token_expired()]
    if len(tokens) > 0:     # Yes, use it
        dv_token = tokens[0]
        dv_token.refresh_token()
    else:                   # No, get a new one
        dv_token = DataverseToken.get_new_token(request.user, app_info, sf)
    
    # return a link to the GeoConnect application, with the token
    #return HttpResponse(dv_token.get_mapit_link_with_token(request))

    return HttpResponseRedirect(dv_token.get_mapit_link_with_token(request))



def view_map_it(request, data_file_md5):
    #return HttpResponse('data_file_id: %s' % data_file_md5)
    
    try: 
        sf = DataFile.objects.select_related('dataset', 'dataset__dataverse').get(md5=data_file_md5)
    except DataFile.DoesNotExist:
        return Http404('file not found for: %s' % data_file_md5)

    json_info = MetadataHelper.get_singlefile_metadata(sf, request, as_json=True)
    if json_info is None:
        # log it
        raise Exception('Failed to create json info')

    return HttpResponse(json_info, content_type="application/json")
    
    
    
    
    
    
    
    
    
    
    