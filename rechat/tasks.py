# -*- coding: utf-8 -*-

from celery import task
from celery_once import QueueOnce
from changefeed.orm import R
from changefeed.tasks import push_to_db
from rechat.conf import DEFAULT_DB, DEFAULT_TABLE


def push_to_chat(data, database=DEFAULT_DB, table=DEFAULT_TABLE):
    push_to_db(database, table, data)
    return

@task(base=QueueOnce, once={'graceful': True, 'keys': []})
def rechat_listener(database=DEFAULT_DB, table=DEFAULT_TABLE):   
    R.listen(database, table, handler='rechat.r_handlers')
    return