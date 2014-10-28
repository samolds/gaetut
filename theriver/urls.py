from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('env.urls')),
    (r'^admin/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
)

handler403 = 'env.views.error.err_403'
handler404 = 'env.views.error.err_404'
handler500 = 'env.views.error.err_500'

if settings.DEBUG:
    urlpatterns += patterns('',
      url(r'^images/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
      }),
    )

urlpatterns += staticfiles_urlpatterns()
