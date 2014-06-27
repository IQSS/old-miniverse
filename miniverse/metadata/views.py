import json

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

from django.core.urlresolvers import reverse
from .meta_services import LinkChecker
from .models import GeographicMetadata

@login_required
def make_link_check(request):
    """
    Check if links are still valid.  
    Doesn't take into consideration new links, etc; more for show.
    Would be an early a.m. cron job
    """
    l = GeographicMetadata.objects.filter(links_working=True)
    ids_to_remove = []
    for meta_info in l:
        LinkChecker.verify_links(meta_info)
        if not meta_info.links_working:
            ids_to_remove.append(meta_info.id)
        
    json_str = json.dumps({'success' : True\
                           , 'ids_to_remove' : ids_to_remove\
                })
    return HttpResponse(json_str, content_type="application/json")

    
# Create your views here.
@login_required
def view_review_map_links(request):
    
    l = GeographicMetadata.objects.filter(links_working=True).select_related('datafile__dataset__dataverse').all()
    d = {'links' : l\
        , 'page_title' : 'Links to WorldMap   '}
    
    return render_to_response('view_review_map_links.html', d\
                                , context_instance=RequestContext(request))
    
    
    return HttpResponse('view_review_map_links')