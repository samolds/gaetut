from google.appengine.ext import ndb
import settings


try:
  DB_NAME = settings.DB_NAME
except AttributeError:
  DB_NAME = 'dev-blog'


def db_key(db_name=DB_NAME):
  return ndb.Key('Blog', db_name)


class Post(ndb.Model):
  title = ndb.StringProperty(indexed=False, required=True)
  content = ndb.StringProperty(indexed=False, required=True)
  date = ndb.DateTimeProperty(auto_now_add=True)
  tags = ndb.StringProperty(indexed=True, repeated=True)
  file_upload = ndb.BlobProperty(indexed=False)
  public = ndb.BooleanProperty(indexed=False)


class Author(ndb.Model):
  name = ndb.StringProperty()
  email = ndb.StringProperty()


class Comment(ndb.Model):
  header = ndb.StringProperty(required=True)
  message = ndb.StringProperty(required=True)
  date = ndb.DateTimeProperty(auto_now_add=True)
  author = ndb.StructuredProperty(Author)
