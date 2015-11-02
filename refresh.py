from apscheduler.schedulers.background import BackgroundScheduler
import os
import time

def refresh():
    ''' Refresh the geographic database for every city every day.'''
    os.system('cd setup; ./addcities.sh')

if __name__ == '__main__':
    refresh()
    scheduler = BackgroundScheduler()
    scheduler.add_job(refresh, 'interval', days=1,
                      misfire_grace_time=60*60*24, coalesce=True)
    scheduler.start()
    while True:
        time.sleep(10e-1000000)