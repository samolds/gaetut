from django.conf.urls import patterns, include, url
from django.contrib import admin
#from django.conf.urls.defaults import *
import dbindexer

handler500 = 'djangotoolbox.errorviews.server_error'

# django admin
admin.autodiscover()

# search for dbindexes.py in all INSTALLED_APPS and load them
dbindexer.autodiscover()

urlpatterns = patterns('views',
    url(r'^$', 'home.home'),
    url(r'^hub$', 'hub.hub'),
    url(r'^about$', 'about.about'),
    url(r'^contact$', 'contact.contact'),
    url(r'^me$', 'personal.personal'),
    url(r'^work$', 'professional.professional'),
    url(r'^school$', 'education.education'),
    url(r'^blog$', 'blog.blog'),
    url(r'^blog/archive$', 'blog.post_archive'),
    url(r'^blog/post(?:/(?P<post_id>\d+))?$', 'blog.post'),
    url(r'^blog/filter(?:/(?P<kind>(\w+[+]*)*))?(?:/(?P<tag>(\w+[-*+]*)*))?$', 'blog.filter'),
    url(r'^river$', 'river.river'),
    url(r'^quotes$', 'quote.quote'),
    url(r'^art$', 'art.art'),
    url(r'^art/archive$', 'art.art_archive'),
    url(r'^art/work(?:/(?P<image_id>\d+))?$', 'art.art_work'),
    url(r'^art/filter(?:/(?P<kind>(\w+[+]*)*))?(?:/(?P<tag>(\w+[-*+]*)*))?$', 'art.filter'),
    url(r'^sha1$', 'sha1.sha1'),

    #url(r'^403$', 'error.err_403'),  # for testing
    #url(r'^404$', 'error.err_404'),  # for testing
    #url(r'^500$', 'error.err_500'),  # for testing
)

urlpatterns += patterns('',
    (r'^admin/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
)
