#!/bin/bash

ls
# frontail -d audit-log.txt
# python3 flasklogreader.py
gunicorn flasklogreader:app --worker-class gevent --bind 0.0.0.0:5000