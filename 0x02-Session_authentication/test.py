#!/usr/bin/env python3


from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def index():
    username = request.cookies.get('mosh')
    return "hello {}!".format(username)

if __name__ == '__main__':
    app.run()
