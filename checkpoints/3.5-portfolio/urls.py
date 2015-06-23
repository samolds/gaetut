import webapp2
from controllers import home
import settings


app = webapp2.WSGIApplication([
  ('/', home.Home),
], debug=settings.DEBUG)
