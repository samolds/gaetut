from controllers.base import BaseRequestHandler
from google.appengine.api import users


class Admin(BaseRequestHandler):
  def get(self):
    user = users.get_current_user()

    if user:
      url = users.create_logout_url(self.request.uri)
      url_linktext = 'Logout'
    else:
      url = users.create_login_url(self.request.uri)
      url_linktext = 'Login'

    self.generate("admin.html", {
      "url": url,
      "url_linktext": url_linktext,
    })
