from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Universe!'

@app.route('/team')
def about():
    return 'Team Name: I have 2 members'
