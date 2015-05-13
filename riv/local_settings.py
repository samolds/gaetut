# Django local_settings for samster project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG
#PRODUCTION_READY = not DEBUG

ADMINS = (
    ('First Last', 'no@reply.com'),
)

MANAGERS = ADMINS

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

CONTACT_EMAIL_RECIPIENT = ["no@reply.com"]

DEFAULT_FROM_EMAIL = 'no@reply.com'
SITENAME = "Google App Engine Django Tutorial"
EMPTY_TEXT = "The text displayed for pages with no text"

# For 'The River' Page --------------------------------

TWITTER = {
    'CONSUMER_KEY': '',
    'CONSUMER_SECRET': '',
    'ACCESS_TOKEN_KEY': '',
    'ACCESS_TOKEN_SECRET': ''
}

SOUNDCLOUD = {
    'CLIENT_ID': '',
    'USER_ID': ''
}

LASTFM = {
    'KEY': '',
    'SECRET': '',
    'USERNAME': ''
}

FLICKR = {
    'KEY': '',
    'SECRET': '',
    'USER_ID': '',
    'USERNAME': ''
}

LINKEDIN = {
    'USERNAME': ''
}

GITHUB = {
    'USERNAME': ''
}

IMGUR = {
    'CLIENT_ID': '',
    'SECRET': '',
    'ACCESS_CODE': '',
    'USERNAME': ''
}

FACEBOOK = {}  # Abandoning. Too hard. I don't know how. Facebook sucks.

# -----------------------------------------------------


# Make this unique, and don't share it with anybody.
SECRET_KEY = 'e8&dhg8y7885jk4ov&!7)f4dqxtm_g-i1-q9j@)4ms@bg^c-t3'

