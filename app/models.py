from google.appengine.ext import ndb
import settings


try:
  BLOG_NAME = settings.BLOG_NAME
except AttributeError:
  BLOG_NAME = 'dev-blog'


def blog_key(blog_name=BLOG_NAME):
  return ndb.Key('Blog', blog_name)


class Post(ndb.Model):
  title = ndb.StringProperty(indexed=False)
  content = ndb.StringProperty(indexed=False)
  date = ndb.DateTimeProperty(auto_now_add=True)
