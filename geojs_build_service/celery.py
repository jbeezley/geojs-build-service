from __future__ import absolute_import

from celery import Celery

app = Celery('geojs')
app.conf.update(
    CELERY_TASK_SERIALIZER='json',
    CELERY_RESULT_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['json']
)

try:
    import celeryconfig  # noqa
    app.config_from_object('celeryconfig')
except ImportError:
    print('import celeryconfig failed, using defaults')

if __name__ == '__main__':
    app.start()
