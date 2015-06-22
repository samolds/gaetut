from controllers.base import BaseRequestHandler
from models import DB_NAME
from models import db_key 
from models import Author
from models import Comment


class Home(BaseRequestHandler):
  def get(self):
    self.generate("home.html")


class About(BaseRequestHandler):
  def get(self):
    self.generate("about.html")


class Contact(BaseRequestHandler):
  def get(self):
    query = Comment.query(ancestor=db_key(DB_NAME)).order(-Comment.date)
    comments = query.fetch(10)
    self.generate("contact.html", {
      "comments": comments
    })

  def post(self):
    comment = Comment(parent=db_key(DB_NAME))
    comment.author = Author(parent=db_key(DB_NAME))
    comment.header = self.request.get('header')
    comment.message = self.request.get('message')
    comment.author.email = self.request.get('email')
    comment.author.name = self.request.get('name')
    comment.put()
    self.redirect('')
