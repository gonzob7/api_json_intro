import requests
from flask import Flask

app = Flask(__name__)

@app.route('/joke')

def get_joke():
    params = {'limitTo':'nerdy'}

    r = requests.get('http://api.icndb.com/jokes/random',params=params)
    joke_json = r.json()

    joke_string = joke_json['value']['joke']
    return joke_string
