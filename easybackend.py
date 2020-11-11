from flask import Flask,request
from bs4 import BeautifulSoup
import requests
import json
import random

app = Flask(__name__)    

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.get_json().get('events')[0]
        print(message) 
        replyToken = message.get('replyToken')      
        print('replyToken:',replyToken)
        messageType =message.get('message').get('type')
        replyData={
            "replyToken":replyToken,
            "messages":[
                {
                "type": messageType,
                }
            ]
        }
        if messageType == 'text':
            text = message.get('message').get('text')
            fist =['剪刀','石頭','布']
            if text in fist:
                ai = random.randint(0,2)
                player = fist.index(text)
                if ai == player:
                    replyMessage='電腦出'+fist[ai]+'，平手'
                elif (ai == 0 and player == 1) or (ai == 1 and player == 2) or (ai == 2 and player ==0):
                    replyMessage='電腦出'+fist[ai]+'，您贏了！'
                else:
                    replyMessage='電腦出'+fist[ai]+'，電腦獲勝！'
            
            if text == 'news' :
                replyMessage ='googleNews'
                replyData['messages'][0]['text'] = replyMessage
            else:
                replyMessage = text
                replyData['messages'][0]['text'] = replyMessage
        elif messageType == 'sticker':
            replyData['messages'][0]["packageId"]='1'
            replyData['messages'][0]["stickerId"]='1'


        ####################################################
        ####################reply user######################
        ####################################################
        accessToken='RUZ1+o+NDKgL7fMvnWovLobOXb0uODZztwcUFrirbtp2OvQqIqO+RMj2vb9ANr7j2Lp7e0Qhujw8RhCM5t1abqXb05K+DacExP8oPd6ONWosy1vbm5zq5gZRWriPHVvu24oBg37U+06b+NKX0sidjAdB04t89/1O/w1cDnyilFU='
        headers={
            'Content-Type':'application/json',
            'Authorization':'Bearer '+accessToken
        }
        data = replyData
        url = 'https://api.line.me/v2/bot/message/reply'
        r = requests.post(url,headers=headers,data=json.dumps(data))

        ####################################################

        return "post"
    if request.method == 'GET':
        return "get"

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000)