from apscheduler.schedulers.background import BackgroundScheduler
import requests

def sensor():
  r = requests.get('https://sleepy-dawn-70030.herokuapp.com/')
  print(r.text)
    

def SchedulerWakeUp():
  sched = BackgroundScheduler(daemon=True)
  sched.add_job(sensor,'cron',day_of_week='0-6', hour='0-23', minute='0-59', second='0,10,20,30,40,50',start_date='2020-11-12')
  sched.start()
  return ''