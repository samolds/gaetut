from google.appengine.api import users
from controllers.base import BaseRequestHandler
import urllib

from models import DEFAULT_GUESTBOOK_NAME
from models import guestbook_key
from models import Author
from models import Greeting


class Greet(BaseRequestHandler):
  def get(self):
    guestbook_name = self.request.get('guestbook_name', DEFAULT_GUESTBOOK_NAME)
    greetings_query = Greeting.query(ancestor=guestbook_key(guestbook_name)).order(-Greeting.date)
    greetings_obj = greetings_query.fetch(10)

    user = users.get_current_user()
    greetings = []
    for greeting in greetings_obj:
      if greeting.author:
        if user and user.user_id() == greeting.author.identity:
          author = greeting.author.email + ' (You)'
        else:
          author = greeting.author.email
      else:
        author = "An anonymous person"
      greetings.append({
        "author": author,
        "content": greeting.content,
      })

    if user:
      url = users.create_logout_url(self.request.uri)
      url_linktext = 'Logout'
    else:
      url = users.create_login_url(self.request.uri)
      url_linktext = 'Login'

    self.generate("greet.html", {
      "greetings": greetings,
      "guestbook_name": guestbook_name,
      "url": url,
      "url_linktext": url_linktext,
    })


  def post(self):
    guestbook_name = self.request.get('guestbook_name', DEFAULT_GUESTBOOK_NAME)
    greeting = Greeting(parent=guestbook_key(guestbook_name))

    if users.get_current_user():
      greeting.author = Author(
          identity=users.get_current_user().user_id(),
          email=users.get_current_user().email())

    greeting.content = self.request.get('content')
    greeting.put()

    query_params = {'guestbook_name': guestbook_name}
    self.redirect('/greet?' + urllib.urlencode(query_params))
