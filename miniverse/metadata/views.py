from django.shortcuts import render_to_response
from django.template import RequestContext

from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

from .models import GeographicMetadata

# Create your views here.
@login_required
def view_review_map_links(request):
    
    l = GeographicMetadata.objects.filter(links_working=True).select_related('datafile__dataset__dataverse').all()
    d = {'links' : l\
        , 'page_title' : 'Links to WorldMap   '}
    
    return render_to_response('view_review_map_links.html', d\
                                , context_instance=RequestContext(request))
    
    
    return HttpResponse('view_review_map_links')