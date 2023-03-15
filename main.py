from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():
    a = request.json['a']
    b = request.json['b']
    return str(a + b)


app.run()