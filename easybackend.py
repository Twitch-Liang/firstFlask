from flask import Flask,request
import requests
import json

app = Flask(__name__)    

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.get_json().get('events')[0]
        print(message) 
        replyToken = message.get('replyToken')      
        print('replyToken:',replyToken)
        text = message.get('message').get('text')      
        print('text:',text)






        ####################################################
        ####################reply user######################
        ####################################################
        accessToken='RUZ1+o+NDKgL7fMvnWovLobOXb0uODZztwcUFrirbtp2OvQqIqO+RMj2vb9ANr7j2Lp7e0Qhujw8RhCM5t1abqXb05K+DacExP8oPd6ONWosy1vbm5zq5gZRWriPHVvu24oBg37U+06b+NKX0sidjAdB04t89/1O/w1cDnyilFU='
        headers={
            'Content-Type':'application/json',
            'Authorization':'Bearer '+accessToken
        }
        data ={
            "replyToken":replyToken,
            "messages":[
            {
                "type":"text",
                "text":text
            },
            {
                "type": "sticker",
                "packageId": "11537",
                "stickerId": "52002749"
            }
        ]
    }
        url = 'https://api.line.me/v2/bot/message/reply'
        r = requests.post(url,headers=headers,data=json.dumps(data))

        ####################################################

        return "post"
    if request.method == 'GET':
        return "get"

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000)