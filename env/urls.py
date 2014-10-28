from django.conf.urls import patterns, include, url

urlpatterns = patterns('env.views',
    #url(r'^$', 'home.home'),
    url(r'^hub$', 'hub.hub'),
    #url(r'^about$', 'about.about'),
    #url(r'^blog$', 'blog.blog'),
    #url(r'^blog/archive$', 'blog.post_archive'),
    #url(r'^blog/post(?:/(?P<post_id>\d+))?$', 'blog.post'),
    #url(r'^river$', 'river.river'),
    #url(r'^quotes$', 'quote.quote'),

    #url(r'^river/async/blogs$', 'river.blogs'),
    #url(r'^river/async/flickrs$', 'river.flickrs'),
    #url(r'^river/async/githubs$', 'river.githubs'),
    #url(r'^river/async/lastfms$', 'river.lastfms'),
    #url(r'^river/async/soundclouds$', 'river.soundclouds'),
    #url(r'^river/async/twitters$', 'river.twitters'),
)
