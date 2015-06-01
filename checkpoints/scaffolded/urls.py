import webapp2
from controllers import home
from controllers import second
import settings


app = webapp2.WSGIApplication([
  ('/', home.Home),
  ('/two', second.Second),
], debug=settings.DEBUG)
