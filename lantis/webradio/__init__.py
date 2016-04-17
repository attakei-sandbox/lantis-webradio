# -*- coding:utf8 -*-
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


class ChannelNotFound(Exception):
    @property
    def message(self):
        return 'Channel "{}" is not found.'.format(self.args[0])

    def __str__(self):
        return repr(self.message)
