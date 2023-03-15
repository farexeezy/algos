from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():
    a = request.json['data']
    return {'sum': sum(a)}

app.run()