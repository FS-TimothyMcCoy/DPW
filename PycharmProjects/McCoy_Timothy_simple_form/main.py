#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        print "Day 5 Form"
        myapp = MyApp(self)


# -------- Dont Touch --------#


class MyApp(object):
    def __init__(self, app):
        print "My app started"
        p = Page()
        p.title = "Form Lab"
        if app.request.GET:
            self.user = app.request.GET['user']
            self.email = app.request.GET['email']
            self.message = app.request.GET['message']
            app.response.write(p.form_exists(self.user, self.email, self.message))
        else:
            app.response.write(p.print_out())





class Page(object):
    def __init__(self):
        self.title = ""
        self.head = '''
<html>
    <head>
        <title>{self.title}</title>
        <link type="text/css" rel="stylesheet" href="/css/main.css" />
    </head>
    <body>
        '''
        self.body = '''
    <h1>Lab Form</h1>
    <div id="wrapper">
    <div id="textside">
    <h2>Hello Scott</h2>
    <p>Welcome to my form! Feel free to browse around the form or submit it.</p>
    </div>
    <div id="formside">
    <form method = "get">
        <label><input type="text" placeholder="Name" name="user" required style="font-style: italic;"></label>
          <label><input type="text" placeholder="Email" name="email" required style="font-style: italic;"></label>
        <textarea name="message" placeholder="Tell us what's on your mind." required style="font-style: italic;"></textarea>
            <button type="submit">Submit</button>
    </form>
    </div>
    </div>
        '''

        self.close = '''
    </body>
</html>

        '''

    def print_out(self):
        return (self.head + self.body + self.close).format(**locals())
    def form_exists(self, user, email, message):
        self.body = '''
        <div id="resultmessage">
        <h1>Our Response: </h1>
        <p>Hello {user}, we will email you at {email} about your message which shows that you said "{message}." If we dont get back to you immediately call us at 1-800-5555</p></div>'''
        return (self.head + self.body + self.close).format(**locals())










app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
