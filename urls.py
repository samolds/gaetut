from django.conf.urls.defaults import *
from django.contrib.auth.forms import AuthenticationForm

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/', }),
    (r'^/', include('sam.urls'))

    #(r'^accounts/create_user/$', 'sam.views.create_new_user'),
    #(r'^accounts/login/$', 'django.contrib.auth.views.login',
    #    {'authentication_form': AuthenticationForm,
    #    'template_name': 'sam/login.html',}),
    (r'^admin/logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/',}),
)
