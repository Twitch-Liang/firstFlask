from apscheduler.schedulers.background import BackgroundScheduler

def print_text():
  print('Waken!')
    

def SchedulerWakeUp():
  sched = BackgroundScheduler(daemon=True)
  sched.add_job(print_text,'interval',seconds=10,start_date='2020-11-12 00:00')
  sched.start()
  return ''