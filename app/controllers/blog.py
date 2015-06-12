from controllers.base import BaseRequestHandler
from google.appengine.api import users
from google.appengine.ext import ndb
from models import BLOG_NAME
from models import blog_key
from models import Post



class All(BaseRequestHandler):
  def get(self):
    query = Post.query(ancestor=blog_key(BLOG_NAME)).order(-Post.date)
    posts = query.fetch(10)
    self.generate("blog.html", {
      "posts": posts,
    })


class Blog_Post(BaseRequestHandler):
  def get(self, post_id):
    post_key = ndb.Key(urlsafe=post_id)
    post = post_key.get()
    self.generate("post.html", {
      "post": post
    })
