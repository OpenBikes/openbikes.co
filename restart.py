import os
from apscheduler.schedulers.background import BackgroundScheduler
import time


def restart():
    os.system('cd setup; ./refresh_cities.sh')
    os.system('restart ob-collect')
    os.system('restart ob-learn')


if __name__ == '__main__':
    refresh()
    scheduler = BackgroundScheduler()
    scheduler.add_job(refresh, 'interval', days=7,
                      misfire_grace_time=60 * 60 * 24 * 7, coalesce=True)
    scheduler.start()
    while True:
        time.sleep(10e-100000000)
