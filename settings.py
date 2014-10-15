from djangoappengine.settings_base import *

import os

INSTALLED_APPS = (
    'djangoappengine',
    'djangotoolbox',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'sam',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
)

LOGIN_REDIRECT_URL = '/sam/'

ADMIN_MEDIA_PREFIX = '/static/admin/'
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'static')
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'),)

ROOT_URLCONF = 'urls'

try:
    from local_settings import *
except ImportError:
    pass
