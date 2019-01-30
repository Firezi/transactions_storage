from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tr_storage.settings')

app = Celery('tasks')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'poll-blocks': {
        'task': 'api.tasks.poll_blocks',
        'schedule': datetime.timedelta(seconds=5)
    }
}
