from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings

def all(request):
  message = "hello world"

  return render_to_response('blog.html', {
      "message": message, 
      "sitename": settings.SITENAME
  }, context_instance=RequestContext(request))
