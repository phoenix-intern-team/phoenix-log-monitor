from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import send, emit
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("socket.html")

@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))

@socketio.on('message')
def handle_message(message):
    send(message)

@socketio.on('stream')
def stream_tail():
    import tailer 	
    print("Executing?")
    f = open('log_files/phoenix-server-log.log', 'r')
    print("Opened file?")
    # prev_lines = tailer.tail(f, 5)
    # sse.publish(json.loads(str(prev_lines)), type='logstream')
    for line in tailer.follow(f):
        print("In tailer?")
        emit('logstream', json.loads(line))