from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():
    a = request.get_json()
    return {'sum': sum(a.values())}

app.run()