from flask import Flask
from threading import Thread

"""
to keeep my server running we can import uptime robot to constantly ping our server

I want to see if there is a way to do this without uptime robot
"""

app = Flask('')

@app.route('/')
def home():
    return "Hello, I am alive"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()