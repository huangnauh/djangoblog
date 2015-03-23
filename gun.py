import os
from multiprocessing import cpu_count
bind = '127.0.0.1:8007'
backlog = 2048
debug = True
proc_name = 'gunicorn.proc'
pidfile = '/tmp/gunicorn.pid'
logfile = '/var/log/gunicorn/debug.log'
loglevel = 'debug'

def max_workers():
    return cpu_count()+1

max_requests = 10000
workers = max_workers()
worker_class = "gevent"

def post_fork(server,worker):
    from psycogreen.gevent import patch_psycopg 
    patch_psycopg()

