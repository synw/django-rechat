# -*- coding: utf-8 -*-

from rechat.conf import USE_HISTORY


if USE_HISTORY is True:
    from rechat.tasks import rechat_listener
    from rechat.conf import DEFAULT_DB, DEFAULT_TABLE

    rechat_listener.delay(DEFAULT_DB, DEFAULT_TABLE)