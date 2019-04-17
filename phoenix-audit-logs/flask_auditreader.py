import os
import flask
from flask import Flask,request,jsonify,render_template,flash,redirect
from flask_restful import Api,Resource,reqparse
import json
import requests


app = Flask(__name__)
json_data=[]
app.config['JSON_SORT_KEYS'] = False

@app.route('/hello',methods=['GET'])
def hello():
    return redirect('log')

@app.route('/log', methods=['GET'])
def log():
    log_file='C:\\Log Monitoring\\audit-log\\audit_log.json'
    json_data=[]
    with open(log_file) as f:
        json_data = json.load(f)
        # for line in f:
        #     json_data.append(json.dumps(line))
    return jsonify(json_data)

@app.route('/logtable',methods = ['GET'])
def result():
    # flash("flash test!!!!")
    return render_template("logtable.html")
    
if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(debug=True,port=1000)