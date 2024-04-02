from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eazzy.settings')

# Create default Celery app
app = Celery("django_celery_project")

# namespace='CELERY' means all celery-related configuration keys
# should be uppercase and have a `CELERY_` prefix in Django settings.
# https://docs.celeryproject.org/en/stable/userguide/configuration.html
app.conf.enable_utc = False
app.conf.update(timezone="Asia/Almaty")
app.config_from_object(settings, namespace="CELERY")

# When we use the following in Django, it loads all the <appname>.tasks
# files and registers any tasks it finds in them. We can import the
# tasks files some other way if we prefer.
app.conf.beat_schedule = {
    'check-event-everyday-at-00': {
        'task': 'sdu_dorm.tasks.check_event',
        'schedule': crontab(hour="0", minute="0"),
    }
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
