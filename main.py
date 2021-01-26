#!/usr/bin/env python

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hey ricky, I worked and I want to show this to you!!!!!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)