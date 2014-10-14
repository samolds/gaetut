# Django local_settings for samsite project.

ADMINS = (
    # ('First Last', 'no@reply.com'),
)

MANAGERS = ADMINS

CONTACT_EMAIL_RECIPIENT = ["no@reply.com"]
DEFAULT_FROM_EMAIL = 'no@reply.com'
USERNAME = "username"
SITENAME = "sitename.com"
PROPER_NAME = "PROPER NAME"
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
    'SECRET': ''
}

FLICKR = {
    'KEY': '',
    'SECRET': '',
    'USER_ID': '@N05'
}

IMGUR = {
    'CLIENT_ID': '',
    'SECRET': '',
    'ACCESS_CODE': ''
}

GITHUB = {} # Only need github username
FACEBOOK = {}  # Abondoning. Too hard. I don't know how. Facebook sucks.

# -----------------------------------------------------


# Make this unique, and don't share it with anybody.
SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
