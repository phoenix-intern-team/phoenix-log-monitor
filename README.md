##Run instructions: 

Start redis server and run the following command:

'''
gunicorn flasklogreader:app --worker-class gevent --bind 0.0.0.0:5000
'''

Open /stream_tail and /logtable concurrently to run live logs