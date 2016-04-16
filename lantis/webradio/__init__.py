# -*- coding:utf8 -*-
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


URL_BASE = 'http://lantis-net.com/'
INDEX_URL = 'http://lantis-net.com/index.html'


class ChannelNotFound(Exception):
    pass
