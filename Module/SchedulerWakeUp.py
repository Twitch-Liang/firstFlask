from apscheduler.schedulers.background import BackgroundScheduler
import requests
import atexit
import os


def sensor():
  r = os.environ.get('MYURL',None)
  print(r.text)
    

def SchedulerWakeUp():
  sched = BackgroundScheduler(daemon=True)
  sched.add_job(sensor,'cron',day_of_week='0-6', hour='0-23', minute='0,10,20,30,40,50', second='0',start_date='2020-11-12')
  sched.start()
  atexit.register(lambda: sched.shutdown())
  return ''