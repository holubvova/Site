import os

from celery import Celery
from celery.schedules import crontab
from celery import shared_task
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Site.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
app = Celery('Site')




# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')



# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'cron_tabs-1-hour':
        {
            'task': 'sendmails.long_task.sendmail_1h',
            'schedule': crontab(minute=0, hour='*/1'),
        },
    'cron_tabs-3-hour':
        {
            'task': 'sendmails.long_task.sendmail_3h',
            'schedule': crontab(minute=0, hour='*/3'),
        },
    'cron_tabs-12-hour':
        {
            'task': 'sendmails.long_task.sendmail_12h',
            'schedule': crontab(minute=0, hour='*/12'),
        },
}


app.conf.timezone = 'UTC'

