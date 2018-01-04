import os
import sys
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

#What methods are we accepting and what URL
@app.route('/post', methods=['POST'])

def webhook():
  data = request.get_json()
  log('Recieved {}'.format(data))

  # We don't want to reply to ourselves! A infinite loop is a result if
  #bot replies to itself. 
  if data['name'] != 'TestBot' and data['text'] == 'on':
     #Light turned on GroupME message
     msg = 'Light has been turned on'
     send_message(msg)
     #Turn Light On
     func1()
  if data['name'] != 'TestBot' and data['text'] == 'off':
    #Light turned off GroupME message
     msg = 'Light has been turned off'
    send_message(msg)
    #Turn Light Off
    func2()

def send_message(msg):
  url  = 'https://api.groupme.com/v3/bots/post'

  data = {
          'bot_id' : "YOUR_BOT_ID_HERE",
          'text'   : msg,
         }
  request = Request(url, urlencode(data).encode())
  json = urlopen(request).read().decode()
  return 'ok', 200

def func1():
  import requests
  headers = {
    'Content-Type': 'application/json',
  }

  params = (
    ('token', 'YOUR_TOKEN_HERE'),
  )

  data = '{"method":"passthrough", "params": {"deviceId": "YOUR_DEVICEID_HERE", "requestData": "{\\"system\\":{\\"set_relay_state\\":{\\"state\\":1}}}" }}'
  response = requests.post('https://use1-wap.tplinkcloud.com/', headers=headers, params=params, data=data)
  m = 'Data sent to TPLink REST API' + data
  log(m)

  return 'ok', 200

def func2():
  import requests
  headers = {
    'Content-Type': 'application/json',
  }

  params = (
    ('token', 'YOUR_TOKEN_HERE'),
  )

  data = '{"method":"passthrough", "params": {"deviceId": "YOUR_DEVICEID_HERE", "requestData": "{\\"system\\":{\\"set_relay_state\\":{\\"state\\":0}}}" }}'
  response = requests.post('https://use1-wap.tplinkcloud.com/', headers=headers, params=params, data=data)
  m = 'Data sent to TPLink REST API' + data
  log(m)

  return 'ok', 200

def log(msg):
  print(str(msg))
  sys.stdout.flush()

