from flask import Flask, request

app = Flask(__name__)


@app.route('/nextround/', methods=['POST'])
def hello_world():
    n = request.json['n']
    k = request.json['k']
    data = request.json['data']
    s = 0
    for i in range(n):
        if data[i] >= data[k] and data[i] > 0:
            s += 1
    return {"res": s}

app.run(host='0.0.0.0', port=5000)