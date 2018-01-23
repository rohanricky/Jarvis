# coding: utf-8
#from gui import MyFrame
import sys
from actions import events,notify
import configparser
import socket
import threading

headers = {'''user-agent':'Chrome/53.0.2785.143'''}
#speak=wicl.Dispatch("SAPI.SpVoice")

#speak = pyttsx.init()
if sys.platform == 'linux':
    notify("Started server")
config = configparser.ConfigParser()
config.read('../config.ini')
host=config['HOST']
sock =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address=('192.168.43.167',5000)
print('starting server on %s and %s' %server_address)
sock.bind(server_address)
sock.listen(1)

while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from ',client_address)
        while True:
            data=connection.recv(256)
            print('received %s' %data)
            if data:
                print(data)
                data=data.decode()
                data=data.lower()
                link=data.split()
                threading.Thread(target=events(data,link)).start()
#                connection.sendall(x.encode())
#                connection.sendall(data)
            else:
                print('no more data')
                break
    finally:
        connection.shutdown(2)
        connection.close()
