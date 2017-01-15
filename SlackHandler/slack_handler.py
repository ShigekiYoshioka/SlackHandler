# -*- coding: utf-8 -*-

from logging.handlers import HTTPHandler

class SlackHandler(HTTPHandler):
    def __init__(self, host, url, token, channel, username):
        super().__init__(host, url, method='POST', secure=True)
        self._token = token
        self._channel = channel
        self._username = username

    def mapLogRecord(self, record):
        ret = {
            "token": self._token,
            "channel": self._channel,
            "text": self.format(record),
            "username": self._username
        }
        return ret
