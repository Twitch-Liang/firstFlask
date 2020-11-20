from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from bs4 import BeautifulSoup
from datetime import time
import requests
import os

from Models.PlayersModel import PlayersModel

from Module.ReplyMessage import ReplyMessage
from Module.PushMessage import PushMessage
from Module.FistGame import FistGame
from Module.SchedulerWakeUp import SchedulerWakeUp
from Module.Rent591 import  Rent591

SchedulerWakeUp()

db = SQLAlchemy()

app = Flask(__name__)

URL=os.environ.get('DATABASE_URL', None)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = URL


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
            
            elif text.find('球員/') != -1:
                name = text.split('/')[1]
                # print(time.now)
                # query = PlayersModel.query.filter_by(name=name).first()
                # print(time.now)
                query = PlayersModel.query.filter(PlayersModel.name.ilike("%" + name + "%")).first()
                if query != None:
                    messages =[
                        {
                        'type':'text',
                        'text': f'{query.name}:{query.from_}~{query.to_}'
                        }
                    ]
                else:
                    messages =[
                    {
                    'type':'text',
                    'text': f'對不起！我沒找到與{name}相關的資料QxQ'
                    }
                ]

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

@app.route('/push')
def push():
    messages =[
        {
        'type':'text',
        'text':'安安安安 測試測試'
        }
            ]
    PushMessage(messages)
    return 'OK'

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000,debug=False,use_reloader=False)