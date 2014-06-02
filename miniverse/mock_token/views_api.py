from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from mock_token.models import DataverseToken
from miniverse_util.json_util import get_json_err, get_json_success
from dataset.mapit_metadata_helper import MetadataHelper
import json

def view_data_file_metadata_base_url(request):
    # place holder in urls file
    raise Http404('not found')
    
def view_data_file_metadata(request, dv_token):
    
    if dv_token is None:
        raise Http404('no token')
        
    try:
        dv_token = DataverseToken.objects.get(token=dv_token)
    except DataverseToken.DoesNotExist:
        return HttpResponse(get_json_err('The token was not found'), content_type="application/json")
        
    if dv_token.has_token_expired():
        json_info = get_json_err('The token has expired.  Please log into dataverse again.')
        print 'json_info', json_info
        return HttpResponse(json_info, content_type="application/json")
   
    json_info = MetadataHelper.get_singlefile_metadata(dv_token.data_file, request)
    
    return HttpResponse(json_info, content_type="application/json")
   
