# -*- coding: utf-8 -*-

import rethinkdb as r
from rechat.conf import DEFAULT_DB, DEFAULT_TABLE


def feed_handlers(database, table, change):
    if database == DEFAULT_DB and table == DEFAULT_TABLE:
        print "--------- CHAT MESSAGE -----------"
        print 'DB: '+str(database)+' - Table: '+str(table)
        print 'Message: '+str(change['new_val'])
    return
