from controllers.base import BaseRequestHandler


class Home(BaseRequestHandler):
  def get(self):
    self.generate("home.html")
