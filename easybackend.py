from flask import Flask,request
from bs4 import BeautifulSoup
from Module.ReplyMessage import ReplyMessage
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
        if messageType == 'text':
            text = message.get('message').get('text')
            print('text:',text)
            fist =['剪刀','石頭','布']
            if text in fist:
                ai = random.randint(0,2)
                player = fist.index(text)
                if ai == player:
                    replyMessage=[
                        {
                            'type':'text',
                            'text':'電腦出'+fist[ai]+'，平手'
                        },
                        {
                            "type": "sticker",
                            "packageId": "11537",
                            "stickerId": "52002773"
                        }
                    ]               
                elif (ai == 0 and player == 1) or (ai == 1 and player == 2) or (ai == 2 and player ==0):
                    replyMessage=[
                        {
                            'type':'text',
                            'text':'電腦出'+fist[ai]+'，您贏了！'
                        },
                        {
                            "type": "sticker",
                            "packageId": "11537",
                            "stickerId": "52002735"
                        } 
                    ] 
                else:
                    replyMessage=[
                        {
                            'type':'text',
                            'text':'電腦出'+fist[ai]+'，電腦獲勝！'
                        },
                        {
                            "type": "sticker",
                            "packageId": "11537",
                            "stickerId": "52002734"
                        }
                    ]
                
            elif text == 'news' :
                replyMessage ='googleNews'
                
            else:
                replyMessage = text
            
        elif messageType == 'sticker':
            replyMessage =[
                        {
                            'type':'sticker',
                            "packageId": "1",
                            "stickerId": "1"
                        }
                    ]


        ReplyMessage(replyToken,message)

        return "post"
    if request.method == 'GET':
        return "get"

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000)