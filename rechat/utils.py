# -*- coding: utf-8 -*-

import json

def jsonify_chat_keys(keys):
    keys_data = []
    for key in keys:
        s = key.split(':')
        timestamp = s[0]
        username = s[1]
        message = s[2]
        keys_data.append({"timestamp":timestamp, "username":username, "message":message})
    return json.dumps(keys_data)