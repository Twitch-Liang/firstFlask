from apscheduler.schedulers.background import BackgroundScheduler
import requests

def sensor():
  r = requests.get('https://sleepy-dawn-70030.herokuapp.com/')
  print(r.text)
    

def SchedulerWakeUp():
  sched = BackgroundScheduler(daemon=True)
  sched.add_job(sensor,'cron',day_of_week='*', hour='*', minute='*', second='0,10,20,30,40,50,60')
  sched.start()
  return ''