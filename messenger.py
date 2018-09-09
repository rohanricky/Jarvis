'''
It is the program to deploy Jarvis to heroku. Currently not working.
'''
import json
import os
import requests
from flask import Flask, request ,Response
import configparser
from scripts import req


#host=config['HOST']
#ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN', config.ACCESS_TOKEN)
VERIFY_TOKEN = os.environ.get('VERIFY_TOKEN', 'xxxyyyzzz')

app = Flask(__name__)


@app.route('/')
def about():
    intro = get_file('static/index.html')
    return Response(intro,mimetype='text/html')

@app.route('/webhook/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        try:
            data=request.get_json()
            return json.dumps(data)
        except:
            return "Fucked Up here"

          # 200 OK
    elif request.method == 'GET':
        if request.args.get('hub.verify_token') == VERIFY_TOKEN:
            return request.args.get('hub.challenge')
        else:
            return 'Error, wrong validation token'

'''
@app.route('/privacy-policy/',methods=['GET'])
def privacy_policy():
    content = get_file('static/privacy-policy.html')
    return Response(content,mimetype='text/html')
'''
def get_file(file):
    try:
        src=os.path.join(root_dir(),file)
        return open(src).read()
    except IOError as exec:
        return str(exec)

def root_dir():
    return os.path.abspath(os.path.dirname(__file__))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)


'''
data = request.get_json(force=True)
messaging_events = data['entry'][0]['messaging']
for event in messaging_events:
    sender = event['sender']['id']
    message = None
    if 'message' in event and 'text' in event['message']:
        if 'quick_reply' in event['message'] and 'payload' in event['message']['quick_reply']:
            quick_reply_payload = event['message']['quick_reply']['payload']
            message = modules.search(quick_reply_payload, sender=sender, postback=True)
        else:
            text = event['message']['text']
            message = modules.search(text, sender=sender)
    if 'postback' in event and 'payload' in event['postback']:
        postback_payload = event['postback']['payload']
        message = modules.search(postback_payload, sender=sender, postback=True)
return

if request.args.get('hub.verify_token') == VERIFY_TOKEN:
    return request.args.get('hub.challenge')
else:
    return 'Error, wrong validation token'

'''
