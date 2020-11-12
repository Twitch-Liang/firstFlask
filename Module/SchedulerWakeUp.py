from apscheduler.schedulers.background import BackgroundScheduler

def print_text():
  print('Waken!')
    

def SchedulerWakeUp():
  sched = BackgroundScheduler(daemon=True)
  sched.add_job(print_text,'interval',seconds=1)
  sched.start()
  return ''