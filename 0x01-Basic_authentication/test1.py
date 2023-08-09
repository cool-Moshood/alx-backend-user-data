#!/usr/bin/env python3

from flask import Flask
from flask_httpauth import HTTPDigestAuth

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MY secret answer here'
auth = HTTPDigestAuth()


user = {
    "mosh": "age",
    "kun": "test",
    "john": "age"
}


@auth.get_password
def get_pwd(username):
    if username in user:
        return user.get(username)
    return None

@app.route('/')
@auth.login_required
def index():
    return "Hello, {}!".format((auth.username()))

if __name__ == '__main__':
    app.run()
