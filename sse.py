import json
from flask import Flask, render_template, jsonify
from flask_sse import sse

import time
import subprocess
import tailer

app = Flask(__name__)
app.config["REDIS_URL"] = "redis://127.0.0.1"
app.config["REDIS_PORT"] = 6379
app.config['JSON_SORT_KEYS'] = False
app.register_blueprint(sse, url_prefix='/stream')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/hello')
def publish_hello():
    sse.publish({"message": "Hello!"}, type='greeting')
    return "Message sent!"

@app.route('/test_for_log')
def log():
    with open ('log_files/phoenix-server-log.log','r') as f:
        json_data=[json.loads(line) for line in f]
    sse.publish(json_data, type='log_stream')
    return jsonify(json_data)

@app.route('/stream_tail')
def stream_tail():
    f = open('log_files/phoenix-server-log.log')
    prev_lines = tailer.tail(f, 1000)
    # sse.publish(json.loads(str(prev_lines)), type='logstream')
    for line in tailer.follow(f):
        # print('output')
        sse.publish(json.loads(line), type='logstream')