from __future__ import absolute_import, unicode_literals
from tr_storage.celery import app


@app.task()
def poll_blocks():
    pass
