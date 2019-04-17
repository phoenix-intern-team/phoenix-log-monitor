import json
import os
from flask import Flask,request,jsonify,render_template,flash
from flask_restful import Api,Resource,reqparse
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


app = Flask(__name__)
json_data=[]
app.config['JSON_SORT_KEYS'] = False

# with open ('phoenix-server-log.log','r') as f:
#     # json_data=[json.loads(line) for line in f]
#     json_data=[json.loads(line) for line in f]

@app.route('/log')
def log():
    with open ('C:/Log Monitoring/log_files/phoenix-server_log-2019-03-19.log','r') as f:
        json_data=[json.loads(line) for line in f]
    return jsonify(json_data)

@app.route('/logtable',methods = ['GET'])
def result():
    # flash("flash test!!!!")
    return render_template("logtable.html")
    


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(debug=True,port=1000)