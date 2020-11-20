from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_mail import Mail
from flask_mail import Message
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



app.config.update(
    #  hotmail的設置
    MAIL_SERVER='smtp.office365.com',
    MAIL_PROT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME'),
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD') 
)
mail = Mail(app)


db.init_app(app)

@app.route("/send_mail")
def SendMail():
    #  主旨
    msg_title = 'Hello It is Flask-Mail'
    #  寄件者，若參數有設置就不需再另外設置
    msg_sender = os.environ.get('MAIL_USERNAME')
    #  收件者，格式為list，否則報錯
    msg_recipients = ['rat800805@gmail.com']
    #  郵件內容
    msg_body = 'Hey, I am mail body!'
    #  也可以使用html
    #  msg_html = '<h1>Hey,Flask-mail Can Use HTML</h1>'
    msg = Message(msg_title,
                  sender=msg_sender,
                  recipients=msg_recipients)
    msg.body = msg_body
    #  msg.html = msg_html
    
    #  mail.send:寄出郵件
    mail.send(msg)
    return 'You Send Mail by Flask-Mail Success!!'




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
    app.run(host='127.0.0.1',port=5000,debug=True,use_reloader=False)