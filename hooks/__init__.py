from flask import Flask, request, jsonify
from hooks.helpers import ResponseProcess

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({'data': {'status': 'OK'}})


@app.route('/hitch-slack', methods=['POST'])
def slack_webhook():
    text = request.form.get('text', '')
    response = ResponseProcess(text)
    return jsonify(text=response.make_response())
