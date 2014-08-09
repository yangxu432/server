from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

# Create your views here.

def index(request):
   ctx = {'value':'values'} 
   return render_to_response('index.html', ctx, context_instance=RequestContext(request))



