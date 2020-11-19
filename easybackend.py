from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from bs4 import BeautifulSoup
from Module.ReplyMessage import ReplyMessage
from Module.FistGame import FistGame
from Module.SchedulerWakeUp import SchedulerWakeUp
from Module.Rent591 import  Rent591
import requests



SchedulerWakeUp()

db = SQLAlchemy()

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://rxtfpqtoiybpuv:6ab1c87f71ee64a09d7dc3700d8fcd0fb12eb0453302a75f8a22df1ffb971012@ec2-52-44-235-121.compute-1.amazonaws.com:5432/d5omf0mtm23h0b"

db.init_app(app)



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
            elif text == 'selfIntroduction':
                messages =[
                    
                ]
            elif text.find('rent591') != -1 :
                messages =Rent591(text)

            else:
                messages =[
                    {
                    'type':'text',
                    'text':text
                    }
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
        return "I'm awake~"

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000,debug=False,use_reloader=False)