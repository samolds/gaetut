from controllers.base import BaseRequestHandler


class About(BaseRequestHandler):
  def get(self):
    self.generate("about.html", {"test": "test2"})
