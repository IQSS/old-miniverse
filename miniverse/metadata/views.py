from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def view_review_map_links(request):
    return HttpResponse('view_review_map_links')