import webapp2
from controllers import home
from controllers import about
import settings


app = webapp2.WSGIApplication([
  ('/', home.Home),
  ('/about', about.About),
], debug=settings.DEBUG)
