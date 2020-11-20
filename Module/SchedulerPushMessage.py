from apscheduler.schedulers.background import BackgroundScheduler
import requests
import atexit
import json
import os

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
        'text':'作業作業 測試測試'
        }
            ]
  }
  url = 'https://api.line.me/v2/bot/message/push'
  r = requests.post(url,headers=headers,data=json.dumps(data))
  

def SchedulerSendPost():
  Scheduler = BackgroundScheduler(daemon=True)
  sched.add_job(sensor,'cron',day_of_week='0-6', hour='10', minute='0', second='0',start_date='2020-11-12',timezone='Asia/shanghai')
  sched.start()
  atexit.register(lambda: Scheduler.shutdown())
  return ''