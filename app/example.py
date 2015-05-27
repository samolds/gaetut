import webapp2

class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.write("Hello, World!")


class SecondPage(webapp2.RequestHandler):
  def get(self):
    self.response.write("New page!")


app = webapp2.WSGIApplication([
  ('/', MainPage),
  ('/two', SecondPage),
], debug=True)
