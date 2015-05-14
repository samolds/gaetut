from django.conf.urls import patterns, include, url

urlpatterns = patterns('river.views',
    url(r'^$', 'home.river'),
    url(r'^blog$', 'blog.all'),
    url(r'^about$', 'about.about'),
    url(r'^contact$', 'contact.contact'),

    url(r'^async/blogs$', 'home.blogs'),
    url(r'^async/flickrs$', 'home.flickrs'),
    url(r'^async/githubs$', 'home.githubs'),
    url(r'^async/lastfms$', 'home.lastfms'),
    url(r'^async/soundclouds$', 'home.soundclouds'),
    url(r'^async/twitters$', 'home.twitters'),
    #url(r'^async/imgurs$', 'home.imgurs'),
    #url(r'^async/facebooks$', 'home.facebooks'),
    #url(r'^async/instagrams$', 'home.instagrams'),
)
