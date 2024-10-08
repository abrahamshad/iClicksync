from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'code_share.settings')

app = Celery('code_share')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

from celery.schedules import crontab

app.conf.beat_schedule = {
    'delete-expired-pastes-every-minute': {
        'task': 'paste.tasks.delete_expired_pastes',
        'schedule': crontab(minute='*/1'),
    },
}
