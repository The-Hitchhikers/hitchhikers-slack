from flask import Flask, request, jsonify
from hooks.helpers import ResponseProcess

app = Flask(__name__)


@app.route('/hitch-slack', methods=['POST'])
def slack():
    text = request.form.get('text', '')
    response = ResponseProcess(text)
    return jsonify(text=response.make_response())
