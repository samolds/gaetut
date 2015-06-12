from google.appengine.api import users
import settings
import webapp2
import jinja2
import os


JINJA_ENVIRONMENT = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'views')),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)


class BaseRequestHandler(webapp2.RequestHandler):
  def generate(self, template_name, template_values={}):

    user = users.get_current_user()
    admin = False
    url_linktext = 'Login'
    url = users.create_login_url(self.request.uri)

    if user:
      admin = True
      url = users.create_logout_url("/")
      url_linktext = 'Logout'

    values = {
      "app_name": settings.APP_NAME,
      "admin": admin,
      "url": url,
      "url_linktext": url_linktext,
    }
    values.update(template_values)
    template = JINJA_ENVIRONMENT.get_template(template_name)
    self.response.out.write(template.render(values, debug=settings.DEBUG))
