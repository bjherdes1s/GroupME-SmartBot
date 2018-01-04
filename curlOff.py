import requests

def func1():
  headers = {
    'Content-Type': 'application/json',
  }

  params = (
    ('token', '93543fb3-71c246da834245d488b8a17'),
  )

  data = '{"method":"passthrough", "params": {"deviceId": "8006C228155C6C83E12C0B0706A5EC18184C53CE", "requestData": "{\\"system\\":{\\"set_relay_state\\":{\\"state\\":0}}}" }}'

  response = requests.post('https://use1-wap.tplinkcloud.com/', headers=headers, params=params, data=data)

func1()
