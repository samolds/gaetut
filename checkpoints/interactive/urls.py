import webapp2
import settings
from controllers import home
from controllers import greet


app = webapp2.WSGIApplication([
  ('/', home.Home),
  ('/greet', greet.Greet),
], debug=settings.DEBUG)
