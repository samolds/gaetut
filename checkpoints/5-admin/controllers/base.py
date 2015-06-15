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
    is_admin = False
    loginout_url = users.create_login_url(self.request.uri)
    loginout_linktext = 'Login'

    if users.is_current_user_admin():
      is_admin = True
      loginout_url = users.create_logout_url("/")
      loginout_linktext = 'Logout'

    values = {
      "APP_NAME": settings.APP_NAME,
      "IS_ADMIN": is_admin,
      "LOGINOUT_URL": loginout_url,
      "LOGINOUT_LINKTEXT": loginout_linktext,
    }
    values.update(template_values)
    template = JINJA_ENVIRONMENT.get_template(template_name)
    self.response.out.write(template.render(values, debug=settings.DEBUG))
