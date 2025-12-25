import os
import logging
from werkzeug.middleware.proxy_fix import ProxyFix
from portcheck import app


class Sendfile2accel(object):
 def __init__(self, app):
  self.app = app

 def __call__(self, environ, start_response):
  def rewrite_response(status, headers, exc_info=None):
   for i, h in enumerate(headers):
    if h[0] == 'X-Sendfile':
     headers[i] = ('X-Accel-Redirect', os.path.abspath(h[1]))
   return start_response(status, headers, exc_info)
  return self.app(environ, rewrite_response)


d = os.path.dirname(os.path.abspath(__file__))
logfile = os.path.join(d, 'log')
file_handler = logging.FileHandler(logfile)
file_handler.setLevel(logging.WARNING)
app.logger.addHandler(file_handler)
app = ProxyFix(app)
app = Sendfile2accel(app)
#We probably should be using this, and have to on the dev server:
#app.wsgi_app = Sendfile2accel(app.wsgi_app)
