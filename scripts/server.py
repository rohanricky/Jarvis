#!/usr/bin/python3

from flask import *
from .actions import events
import threading
import configparser
from . import req
import ctypes
import os
from multiprocessing import Process

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('config.ini')
access_token=config['ACCESS_TOKEN']
pardir=os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)),os.pardir))
#print(pardir)
check = ctypes.CDLL(pardir+'/lib/cpp/libint.so')

@app.route("/api"+access_token['PHONE_TOKEN'],methods=["POST"])
def api():
    data=request.form['data']
    print(data)
    data=data.lower()
    link=data.split()
    Process(target=req,args=(data,)).start()
    return data

if __name__=='__main__':
    host=config['HOST']
#    print(host['Address'])
    app.run(host='0.0.0.0',port=int(host['Port']))
#host='0.0.0.0'
