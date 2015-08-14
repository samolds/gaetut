from google.appengine.ext import ndb
import settings


try:
  DB_NAME = settings.DB_NAME
except AttributeError:
  DB_NAME = 'dev-guestbook'


def guestbook_key(guestbook_name=DB_NAME):
  return ndb.Key('Guestbook', guestbook_name)


class Author(ndb.Model):
  name = ndb.StringProperty(indexed=False)
  email = ndb.StringProperty(indexed=False)


class Greeting(ndb.Model):
  author = ndb.StructuredProperty(Author)
  content = ndb.StringProperty(indexed=False)
  date = ndb.DateTimeProperty(auto_now_add=True)
