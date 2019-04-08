#!/usr/bin/env python3
import json
from flask import Flask,request,jsonify,render_template,flash
from flask_restful import Api,Resource,reqparse
import time
import tailer
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from flask_sse import sse

app = Flask(__name__)
# redis://127.0.0.1 - for ubuntu
# redis://redis:6379 - for docker
app.config["REDIS_URL"] = "redis://redis:6379"
app.config["REDIS_PORT"] = 6379
app.config['JSON_SORT_KEYS'] = False
app.register_blueprint(sse, url_prefix='/stream')
json_data=[]

# with open ('phoenix-server-log.log','r') as f:
#     # json_data=[json.loads(line) for line in f]
#     json_data=[json.loads(line) for line in f]

@app.route('/hello')
def publish_hello():
    sse.publish({"message": "Hello!"}, type='greeting')
    return "Message sent!"

@app.route('/log')
def log():
    # CHANGE LOG FILE PATH HERE
    with open ('log_files/phoenix-log-monitor_logfiles/phoenix-server_log-2019-03-22.log','r') as f:
        json_data=[json.loads(line) for line in f]
    return jsonify(json_data)

@app.route('/getlogs')
def getlogs():
   return render_template('getlogs.html')


@app.route('/logtable',methods = ['GET'])
def result():
    # flash("flash test!!!!")
    return render_template("logtable.html")

@app.route('/stream_tail')
def stream_tail():
    f = open('log_files/phoenix-log-monitor_logfiles/phoenix-server_log-2019-03-22.log')
    # prev_lines = tailer.tail(f, 5)
    # sse.publish(json.loads(str(prev_lines)), type='logstream')
    for line in tailer.follow(f):
        # print('output')
        sse.publish(json.loads(line), type='logstream')

# if __name__ == "__main__":
#     app.secret_key = 'super secret key'
#     app.run(host='0.0.0.0', debug=True,port=5000)