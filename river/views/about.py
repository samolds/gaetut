from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings

def about(request):
  message = "hello world"

  return render_to_response('about.html', {
      "message": message, 
      "sitename": settings.SITENAME
  }, context_instance=RequestContext(request))
