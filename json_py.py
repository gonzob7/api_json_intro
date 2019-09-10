import requests

r = requests.get('http://api.icndb.com/jokes/random?limitTo=nerdy')
joke_json = r.json()

joke_string = joke_json['value']['joke']

print(joke_string)
