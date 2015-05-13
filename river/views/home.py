from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
#from river.models import Post

def home(request):
  message = "hello world"

  return render_to_response('home.html', {
      "message": message, 
      "sitename": settings.SITENAME
  }, context_instance=RequestContext(request))
