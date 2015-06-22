from controllers.base import BaseRequestHandler
from google.appengine.api import users
from google.appengine.ext import ndb
from models import DB_NAME
from models import db_key 
from models import Post



class All(BaseRequestHandler):
  def get(self):
    query = Post.query(ancestor=db_key(DB_NAME)).order(-Post.date)
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


class Filter(BaseRequestHandler):
  def get(self, tag):
    qry = Post.query(Post.tags == tag)
    posts = []
    for post in qry.iter():
      posts.append(post)
    self.generate("blog_filter.html", {
      "posts": posts,
      "tag": tag
    })
