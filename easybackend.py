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
            elif text == 'flex':
                messages =[
                    {
  "type": "flex",
  "altText": "this is a flex message",
  "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_5_carousel.png",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "Arm Chair, White",
            "weight": "bold",
            "size": "xl",
            "wrap": True,
            "contents": []
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "$49",
                "weight": "bold",
                "size": "xl",
                "flex": 0,
                "wrap": True,
                "contents": []
              },
              {
                "type": "text",
                "text": ".99",
                "weight": "bold",
                "size": "sm",
                "flex": 0,
                "wrap": True,
                "contents": []
              }
            ]
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "Add to Cart",
              "uri": "https://linecorp.com"
            },
            "style": "primary"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "Add to wishlist",
              "uri": "https://linecorp.com"
            }
          }
        ]
      }
    }
  ]
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