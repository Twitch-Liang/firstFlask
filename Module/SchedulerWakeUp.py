from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import requests

def sensor():
  r = requests.get('https://sleepy-dawn-70030.herokuapp.com/')
  print(r)
    

def SchedulerWakeUp():
  sched = BackgroundScheduler(daemon=True)
  interval = IntervalTrigger(
        seconds = 5,
        start_date='2020-11-12 00:00:00',
        end_date='2999-12-31 23:59:59',
        timezone='Asia/Shanghai')
  sched.add_job(sensor,trigger=interval)
  sched.start()
  return ''