#!/usr/bin/env python

# Add the lib subdir to the python load path.
# Uses only __import__ to keep from polluting main.py.
# Not beautiful but... yeah.
__import__("sys").path.insert(1, __import__("os.path").path.join(__import__("os.path").path.abspath('.'), 'lib'))

#####
# Begin file in earnest.

import json
import logging

from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=["POST"])
def new_message():
    """
    When a new message is seen, respond with "blah".
    Do not respond to bots.
    """
    if request.form['user_id'] == 'USLACKBOT':
        return ''
    return '{"text": "blah"}'
