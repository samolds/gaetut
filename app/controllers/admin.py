from controllers.base import BaseRequestHandler
from google.appengine.api import users
from google.appengine.ext import ndb
from models import DB_NAME
from models import blog_key
from models import Post




class Panel(BaseRequestHandler):
  def get(self):
    self.generate("admin/panel.html")


class Blog_All(BaseRequestHandler):
  def get(self):
    query = Post.query(ancestor=blog_key(DB_NAME)).order(-Post.date)
    posts = query.fetch()

    self.generate("admin/blog_all.html", {
      "posts": posts,
    })


class Blog_New(BaseRequestHandler):
  def get(self):
    self.generate("admin/blog_new.html")

  def post(self):
    post = Post(parent=blog_key(DB_NAME))
    post.title = self.request.get('title')
    post.content = self.request.get('content')
    post.put()
    self.redirect('/admin/blog')


class Blog_Edit(BaseRequestHandler):
  def get(self, post_id):
    post_key = ndb.Key(urlsafe=post_id)
    post = post_key.get()

    self.generate("admin/blog_edit.html", {
      "post": post
    })

  def post(self, post_id):
    post_key = ndb.Key(urlsafe=post_id)
    post = post_key.get()

    post.title = self.request.get('title')
    post.content = self.request.get('content')
    post.put()
    self.redirect('/admin/blog')


class Blog_Delete(BaseRequestHandler):
  def get(self, post_id):
    post_key = ndb.Key(urlsafe=post_id)
    post_key.delete()
    self.redirect('/admin/blog')
