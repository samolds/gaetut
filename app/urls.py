import webapp2
import settings
from controllers import home
from controllers import file_upload
from controllers import blog
from controllers import admin


app = webapp2.WSGIApplication([
  webapp2.Route(r'/', home.Home),
  webapp2.Route(r'/about', home.About),
  webapp2.Route(r'/blog', blog.All),
  webapp2.Route(r'/blog/all', blog.All),
  webapp2.Route(r'/blog/post/<post_id:[A-Za-z0-9_\-]+$>', blog.Blog_Post),
  webapp2.Route(r'/blog/filter/<tag:[A-Za-z0-9_\-]+$>', blog.Filter),
  webapp2.Route(r'/contact', home.Contact),
  webapp2.Route(r'/file/<file_id:[A-Za-z0-9_\-]+$>', file_upload.File_Upload),

  webapp2.Route(r'/admin', admin.Panel),
  webapp2.Route(r'/admin/blog', admin.Blog_All),
  webapp2.Route(r'/admin/blog/all', admin.Blog_All),
  webapp2.Route(r'/admin/blog/new', admin.Blog_New),
  webapp2.Route(r'/admin/blog/edit/<post_id:[A-Za-z0-9_\-]+$>', admin.Blog_Edit),
  webapp2.Route(r'/admin/blog/delete/<post_id:[A-Za-z0-9_\-]+$>', admin.Blog_Delete),
], debug=settings.DEBUG)
