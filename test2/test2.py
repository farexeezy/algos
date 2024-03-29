import requests

host = 'http://127.0.0.1:5000'
r = requests.post(host,
                  json={'data': [1, 2, 3]})

assert r.json() == {'sum': 6}

r = requests.post(host,
                  json={'data': [-1, -2, -3]})

assert r.json() == {'sum': -6}