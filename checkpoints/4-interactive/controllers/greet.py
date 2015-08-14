from controllers.base import BaseRequestHandler
from models import DB_NAME
from models import guestbook_key
from models import Author
from models import Greeting


class Greet(BaseRequestHandler):
  def get(self):
    query = Greeting.query(ancestor=guestbook_key(DB_NAME)).order(-Greeting.date)
    greetings_obj = query.fetch(10)

    greetings = []
    for greeting in greetings_obj:
      if greeting.author and greeting.author.name:
        author = greeting.author.name
      elif greeting.author and greeting.author.email:
        author = greeting.author.email
      else:
        author = "Anonymous"

      greetings.append({
        "author": author,
        "content": greeting.content,
      })

    self.generate("greet.html", {"greetings": greetings})


  def post(self):
    greeting = Greeting(parent=guestbook_key(DB_NAME))
    user_name = self.request.get('name')
    user_email = self.request.get('email')
    greeting.author = Author(name=user_name, email=user_email)
    greeting.content = self.request.get('content')
    greeting.put()
    self.redirect('/greet')
