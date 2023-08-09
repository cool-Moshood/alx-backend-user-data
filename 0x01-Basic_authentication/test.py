#!/usr/bin/env python3

from flask import Flask
from flask_httpauth import HTTPTokenAuth, HTTPDigestAuth


app = Flask(__name__)
token_auth = HTTPTokenAuth(scheme='Bearer')  # Renamed auth1 to token_auth
digest_auth = HTTPDigestAuth()  # Renamed auth to digest_auth
app.config['SECRET_KEY'] = 'your_secret_key_here'


tokens = {
    "secret-token-1": "john1",
    "secret-token-2": "susan"
}

users = {
    "john": "age",
    "susan": "base"
}

@token_auth.verify_token  # Renamed auth1 to token_auth
def verify_token(token):
    if token in tokens:
        return tokens[token]

@digest_auth.get_password  # Renamed auth to digest_auth
def get_pwd(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/')
@digest_auth.login_required  # Renamed auth to digest_auth
def index():
    # return "Hello {}!".format(digest_auth.username())  # Renamed auth to digest_auth
    return "Hello {}!".format(token_auth.current_user())
if __name__ == '__main__':
    app.run()
