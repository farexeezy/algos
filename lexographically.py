from flask import Flask, request

app = Flask(__name__)


@app.route('/lexographically/', methods=['POST'])
def hello_world():
    a = request.json['a'].lower()
    b = request.json['b'].lower()
    s = 0
    if a == b:
        s = 0
    elif a < b:
        s =+ -1
    else:
        s =+ 1
    return {"res": s}
    

app.run(host='0.0.0.0', port=5000)