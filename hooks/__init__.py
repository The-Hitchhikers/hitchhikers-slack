from flask import Flask, jsonify
from hooks.helpers import ResponseProcess
from slackhook import SlackWebHook

app = Flask(__name__)
slack = SlackWebHook(app, '/hitch-slack')


@app.route('/')
def index():
    return jsonify({'data': {'status': 'OK'}})


@slack.hook()
def slack_webhook(data):
    response = ResponseProcess(data)
    return jsonify(text=response.make_response())
