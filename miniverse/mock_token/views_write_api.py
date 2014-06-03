from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from miniverse_util.json_util import get_json_err, get_json_success_msg

from mock_token.models import DataverseToken
from metadata.forms import GeographicMetadataUpdateForm
from metadata.models import GeographicMetadata

import json


@csrf_exempt
def view_update_gis_metadata(request):
    """
    Given a valid token, return metadata about a single datafile
    
    :rtype: JSON
    """
    
    if request.method=='POST':        
        geo_metadata_form = GeographicMetadataUpdateForm(request.POST)
        if geo_metadata_form.is_valid():
            if geo_metadata_form.save_metadata():
                return HttpResponse(get_json_success_msg('The metadata was saved'))
            else:
                return HttpResponse(get_json_err('The metadata was not saved'))                
        else:
           return HttpResponse(get_json_err('The form was not valid'), content_type="application/json")
           
    return HttpResponse(get_json_err('No updates were submitted'), content_type="application/json")

  