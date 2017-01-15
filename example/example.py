#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from SlackHandler import SlackHandler

slack_handler = SlackHandler(
    host='slack.com',
    url='/api/chat.postMessage',
    token="slack Web API token",
    channel="#general",
    username="slack_handler"
)

logging.basicConfig(level=logging.DEBUG)

fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
datefmt = "%Y/%m/%d %H:%M:%S"
formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)

slack_handler.setFormatter(fmt=formatter)

logger = logging.getLogger('logger')
logger.addHandler(slack_handler)

logger.debug('debug')
logger.info('info')
logger.warning('warning')
logger.error('error')
logger.critical('critical') 
