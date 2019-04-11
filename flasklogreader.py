#!/usr/bin/env python3
import json
import flask
import os
from flask import Flask,request,jsonify,render_template,flash
from flask_restful import Api,Resource,reqparse
import time
import tailer
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from flask_sse import sse
from flask_socketio import SocketIO
from flask_socketio import send, emit

app = Flask(__name__)
# redis://127.0.0.1 - for ubuntu
# redis://redis:6379 - for docker
app.config["REDIS_URL"] = "redis://127.0.0.1"
app.config["REDIS_PORT"] = 6379
app.config['JSON_SORT_KEYS'] = False
# app.register_blueprint(sse, url_prefix='/stream')
socketio = SocketIO(app)

json_data=[]

BASE_DIR = '/home/phoenix-log-monitor/log_files/phoenix-log-monitor_logfiles/'

# with open ('phoenix-server-log.log','r') as f:
#     # json_data=[json.loads(line) for line in f]
#     json_data=[json.loads(line) for line in f]

@app.route('/', methods=['GET','POST'])
def dropdown():
    files = os.listdir(BASE_DIR)
    return render_template('files.html', files=files)

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    select = request.form.get('file')
    sel=str(select)
    res = flask.make_response("cookie set")
    res.set_cookie('file', sel)
    return res

@app.route('/log')
def log():
    # CHANGE LOG FILE PATH HERE
	select = request.cookies.get('file')
	sel=str(select)
	log_file=os.path.join(BASE_DIR,sel)
	with open (log_file,'r') as f:
		json_data=[json.loads(line) for line in f]
	return jsonify(json_data)

@app.route('/getlogs')
def getlogs():
    return render_template('getlogs.html')


@app.route('/logtable',methods = ['GET'])
def result():
    # flash("flash test!!!!")
    return render_template("logtable.html")

@socketio.on('stream')
def stream_tail():
	import tailer
	base_file = request.cookies.get('file')
	print(os.path.join(BASE_DIR,str(base_file)))
	log_file=os.path.join(BASE_DIR,str(base_file))
	f = open(log_file, 'r')
    # prev_lines = tailer.tail(f, 5)
    # sse.publish(json.loads(str(prev_lines)), type='logstream')
	for line in tailer.follow(f):
		emit('logstream', json.loads(line))

# if __name__ == "__main__":
#     app.secret_key = 'super secret key'
#     app.run(host='0.0.0.0', debug=True,port=5000)