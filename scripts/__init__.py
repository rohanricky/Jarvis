import requests
from src import music,sync,lock,identity,launch,search,misc
import sys
import json
import configparser

'''
config = configparser.ConfigParser()
config.read('config.ini')
host=config['HOST']
'''

URL = 'https://api.wit.ai/message?v=27/12/2017&q='
ACCESS_TOKEN='36L4ZZ7QSD6KX3B3SEJGOA5LS4Y53CF6'

def req(input):
    r = requests.post(URL+input, headers={
        'Authorization': 'Bearer %s' %ACCESS_TOKEN
    })

    data = r.json()
    for intent,text in data['entities'].items():
        i=text[0]['value']
        confidence=text[0]['confidence']
    text=data['_text']
    print(text)
    if confidence > 0.7:
        sys.modules['src.'+intent].execute(i)
    else:
        sys.modules['src.misc'].execute(text)
if __name__=='__main__':
    req("adirindi maayo music")
