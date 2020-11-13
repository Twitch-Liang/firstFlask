from flask import Flask,request
from bs4 import BeautifulSoup
from Module.ReplyMessage import ReplyMessage
from Module.FistGame import FistGame
from Module.SchedulerWakeUp import SchedulerWakeUp
import requests


SchedulerWakeUp()

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
            elif text == 'selfIntroduction':
                messages =[
                    {
                        'type':'flex',
                        'altText':'flex text of introduce myself',
                        'contents':{
                            'type':'bubble',
                            'header':{
                                'type':'box',
                                'layout':'vertical',
                                'contents':[
                                    {
                                        'type':'text',
                                        'text':'hello world~',
                                        'size':'xl',
                                        'color':'#15D573FF',
                                        'align':'center',
                                        'contents':[]
                                    }
                                ]
                            },
                            'hero':{
                                'type':'image',
                                'url':'https://www.vjgamer.com.hk/wp-content/uploads/2019/03/22/52331/40452668763_42996d9575_o-900x900.jpg',
                                'size':'full',
                                'aspectRatio':'1.5:1',
                                'aspectMode':'fit'
                            },
                            'body':{
                                'type':'box',
                                'layout':'vertical',
                                'contents':[
                                    {
                                        'type':'text',
                                        'text':'My name is Little_Twitch~',
                                        'align':'center',
                                        'contents':[
                                            {
                                                "type": "span",
                                                "text": "I was born on 2020/11/10!"
                                            }
                                        ]
                                    }
                                ]
                            },
                            # 'footer':{
                            #     'type':'box',
                            #     'layout':'horizontal',
                            #     'contents':[
                            #         {
                            #             'type':'button',
                            #             'action':{
                            #                 'type':'uri',
                            #                 'label':'button',
                            #                 'uri':''
                            #             }
                            #         }
                            #     ]
                            # }
                        }
                    }
                ]
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