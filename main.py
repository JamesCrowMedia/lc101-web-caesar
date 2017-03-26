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
import caesar
import cgi

header = """
    <!DOCTYPE html>
    <html>
        <head>
        <title>Web Caesar</title>
        <style>
            article {
                width: 500px;
                margin: 0px auto 0px auto;
            }

            body {
                font-family: Verdana, sans-serif;
            }

            h1, h2 {
                text-align: center;
            }

            h1 {
                font-size: 40px;
                margin-bottom: .25em;

            }

            h2 {
                font-size: 20px;
                font-weight: 200;
                margin-bottom: 2em;
            }

            form {
                width: 100%;
            }

            textarea {
                width: 100%;
                height: auto;
                max-width: 500px;
                min-height: 300px;
                padding: 10px;
                overflow: auto;
            }

            #submit{
                border-top:		2px solid #A1A1A1;
            	border-left:	2px solid #A1A1A1;
            	border-right:	2px solid #424242;
            	border-bottom:	2px solid #424242;
            	padding:		10px 20px !important;
            	font-size:		14px !important;
            	background-color:	#fff;
            	font-weight:	bold;
            	color:			#000;
                float: right;
                margin-right: -22px;
            }
        </style>
        </head>
        <body>

            <article>
                <h1>Web Caesar</h1>
                <h2>Enter some text to ROT:</h2>
"""

footer = """
            </article>
        </body>
    </html>
"""

def build_page(textarea_content):

    # Form HTML ------------------------
    messageInput = '<label> Type a message:</br> <textarea name="user_message">' + textarea_content + '</textarea></label></br>'
    rotateInput = '<label> Rotate by <input type="text" name="user_rotation" /> letters.</label></br></br>'
    submit = '<input id="submit" type="submit" value="submit" />'
    return '<form method="post">' + rotateInput + messageInput + submit + '</form>'

class MainHandler(webapp2.RequestHandler):
    def get(self):

        # Build Form -----------------------
        form = build_page("")

        # Output ---------------------------
        self.response.write(header + form + footer)

    def post(self):
        # User Input  -----------------------
        message = self.request.get("user_message")
        rotation = self.request.get("user_rotation")
        encrypted_message = caesar.encrypt(message, rotation)
        escaped_message = cgi.escape(encrypted_message)
        # Build Form -----------------------
        form = build_page(escaped_message)

        # Output ---------------------------
        self.response.write(header + form + footer)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
