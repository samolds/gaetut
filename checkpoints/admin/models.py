from google.appengine.ext import ndb
import settings


try:
  DB_NAME = settings.DB_NAME
except AttributeError:
  DB_NAME = 'dev-blog'


def blog_key(blog_name=DB_NAME):
  return ndb.Key('Blog', blog_name)


class Post(ndb.Model):
  title = ndb.StringProperty(indexed=False)
  content = ndb.StringProperty(indexed=False)
  date = ndb.DateTimeProperty(auto_now_add=True)
