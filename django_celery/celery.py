from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery.settings')
app = Celery('django_celery')
app.conf.enable_utc = False
app.conf.update(timezone='Africa/Lagos')
app.config_from_object(settings, namespace='CELERY')

# CELERY BEAT SETTINGS
app.conf.beat_schedule = {
    'send-mail-everyday-at-7am': {
        'task': 'send_mail_app.tasks.send_mail_func',
        'schedule': crontab(hour=12, minute=51),
        # 'schedule': crontab(minute='*/10'), will send every quarter
        # 'args': (2, ) you can pass arguments to your task func here
    }
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')