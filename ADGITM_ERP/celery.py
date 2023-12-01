# celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ADGITM_ERP.settings')

# create a Celery instance and configure it using the settings from Django
app = Celery('ADGITM_ERP')
app.conf.enable_utc = False
app.conf.update(timezone="Asia/Kolkata")
# load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')

# autodiscover tasks in all installed apps
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-emails-every-2-days': {
        'task': 'maintenance_management.tasks.send_email_task',
        # 'schedule': crontab(minute=0, hour=0, day_of_week='*/2'),
        'schedule' : crontab(minute='*')
    },
}
@app.task(bind=True)
def debug_task(self):
    print(f"Request {self.request!r}")
