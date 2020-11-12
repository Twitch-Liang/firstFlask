import requests
import json


def ReplyMessage(replyToken,message):
  accessToken='RUZ1+o+NDKgL7fMvnWovLobOXb0uODZztwcUFrirbtp2OvQqIqO+RMj2vb9ANr7j2Lp7e0Qhujw8RhCM5t1abqXb05K+DacExP8oPd6ONWosy1vbm5zq5gZRWriPHVvu24oBg37U+06b+NKX0sidjAdB04t89/1O/w1cDnyilFU='
  headers={
      'Content-Type':'application/json',
      'Authorization':'Bearer '+accessToken
  }
  data = {
      "replyToken":replyToken,
      "messages":message
  }
  url = 'https://api.line.me/v2/bot/message/reply'
  r = requests.post(url,headers=headers,data=json.dumps(data))
  return r