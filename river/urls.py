from django.conf.urls import patterns, include, url

urlpatterns = patterns('river.views',
    url(r'^$', 'river.river'),
    url(r'^bootstrap$', 'home.bootstrap'),
    #url(r'^hub$', 'hub.hub'),
    #url(r'^about$', 'about.about'),
    #url(r'^contact$', 'contact.contact'),

    url(r'^river/async/blogs$', 'river.blogs'),
    url(r'^river/async/flickrs$', 'river.flickrs'),
    url(r'^river/async/githubs$', 'river.githubs'),
    url(r'^river/async/lastfms$', 'river.lastfms'),
    url(r'^river/async/soundclouds$', 'river.soundclouds'),
    url(r'^river/async/twitters$', 'river.twitters'),
    #url(r'^river/async/$', 'river.imgurs'),
    #url(r'^river/async/$', 'river.facebooks'),
)
