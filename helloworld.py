# from google.appengine.api import users

import webapp2


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.write('Hello World')
        


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
