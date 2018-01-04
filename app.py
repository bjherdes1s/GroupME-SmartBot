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
  #bot replies to itself
  if data['name'] != 'TestBot' and data['text'] == 'on':
     #msg = '{}, you sent "{}".'.format(data['name'], data['text'])
     msg = 'Light has been turned on'
     send_message(msg)
     func1()
  if data['name'] != 'TestBot' and data['text'] == 'off':
    msg = 'Light has been turned off'
    send_message(msg)
    func2()

def send_message(msg):
  url  = 'https://api.groupme.com/v3/bots/post'

  data = {
          'bot_id' : "5e9407c447fbbc988ca2eb7076",
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
    ('token', '93543fb3-71c246da834245d488b8a17'),
  )

  data = '{"method":"passthrough", "params": {"deviceId": "8006C228155C6C83E12C0B0706A5EC18184C53CE", "requestData": "{\\"system\\":{\\"set_relay_state\\":{\\"state\\":1}}}" }}'
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
    ('token', '93543fb3-71c246da834245d488b8a17'),
  )

  data = '{"method":"passthrough", "params": {"deviceId": "8006C228155C6C83E12C0B0706A5EC18184C53CE", "requestData": "{\\"system\\":{\\"set_relay_state\\":{\\"state\\":0}}}" }}'
  response = requests.post('https://use1-wap.tplinkcloud.com/', headers=headers, params=params, data=data)
  m = 'Data sent to TPLink REST API' + data
  log(m)

  return 'ok', 200

def log(msg):
  print(str(msg))
  sys.stdout.flush()

