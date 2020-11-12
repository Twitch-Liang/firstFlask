from flask import Flask,request
from bs4 import BeautifulSoup
from Module.ReplyMessage import ReplyMessage
from Module.FistGame import FistGame
import requests


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
                messages=FistGame(text)
                
            elif text == 'news' :
                messages =[
                    {
                    'type':'text',
                    'text':'googleNews'
                    }
                ]   
            else:
                messages =[
                    'type':'text',
                    'text':text
                ] 
            
        elif messageType == 'sticker':
            messages =[
                        {
                            'type':'sticker',
                            "packageId": "1",
                            "stickerId": "1"
                        }
                    ]
        if message:
            ReplyMessage(replyToken,messages)
        return "post"
    if request.method == 'GET':
        return "get"

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000)