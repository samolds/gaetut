from controllers.base import BaseRequestHandler


class Second(BaseRequestHandler):
  def get(self):
    self.generate("second.html", {"test": "test2"})
