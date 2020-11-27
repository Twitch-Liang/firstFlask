from apscheduler.schedulers.background import BackgroundScheduler
import requests
import json
import os


def sensor():
  url=os.environ.get('MYURL',None)
  r = requests.get(url)
  print(r.text)

def SchedulerPushMessage():
  accessToken=os.environ.get('ACCESS_TOKEN', None)
  headers={
      'Content-Type':'application/json',
      'Authorization':'Bearer '+accessToken
  }
  data = {
      "to": 'Ua4d13e2b37c906baf6bf772d2b213aab',
      "messages":[
        {
        'type':'text',
        'text':'作業作業 終於要成功了...嗎?'
        }
            ]
  }
  url = 'https://api.line.me/v2/bot/message/push'
  r = requests.post(url,headers=headers,data=json.dumps(data))
  print(r)



def SchedulerWakeUp():
  sched = BackgroundScheduler(daemon=True)
  sched.add_job(sensor,'cron',day_of_week='0-6', hour='0-23', minute='0,10,20,30,40,50', second='0',start_date='2020-11-12',timezone='Asia/Taipei')
  # sched.add_job(SchedulerPushMessage,'cron',day_of_week='0-6', hour='10', minute='0', second='0',start_date='2020-11-12',timezone='Asia/Taipei')
  sched.start()
  return ''