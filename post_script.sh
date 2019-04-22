#!/bin/bash

ls
# frontail -d audit-log.txt
# python3 flasklogreader.py
gunicorn flasklogreader:app --worker-class gevent --bind 0.0.0.0:5000
# gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 flasklogreader:app --bind 0.0.0.0:5000