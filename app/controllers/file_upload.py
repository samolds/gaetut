from controllers.base import BaseRequestHandler
from google.appengine.ext import ndb


class File_Upload(BaseRequestHandler):
  def get(self, file_id):
    key = ndb.Key(urlsafe=file_id)
    blog = key.get()
    if blog.file_upload:
      self.response.headers['Content-Type'] = 'image/gif'
      self.response.out.write(blog.file_upload)
    else:
      self.response.out.write('No file')
