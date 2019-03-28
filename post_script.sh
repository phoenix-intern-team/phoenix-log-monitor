#!/bin/bash

ls
frontail -d log_files/phoenix-server-log.log
python3 flasklogreader.py