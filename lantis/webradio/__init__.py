# -*- coding:utf8 -*-
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


URL_BASE = 'http://lantis-net.com/'
INDEX_URL = 'http://lantis-net.com/index.html'


class ChannelNotFound(Exception):
    pass


class Channel(object):
    def __init__(self, site_url, title, last_episode_url):
        self.title = title
        self.site_url = site_url
        self.last_episode_url = last_episode_url
        self.channel_id = site_url.replace(URL_BASE, '')[:-1]

    def __repr__(self):
        return self.title

    @classmethod
    def from_html(cls, dom):
        """Generate instance from BeautifulSoup object
        """
        title_ = dom.h3.a.string
        lsite_url_ = dom.h3.a.get('href')
        episode_url_ = dom.p.find_all('a')[1].get('href')
        obj = cls(lsite_url_, title_, episode_url_)
        return obj

    @classmethod
    def find(cls, key):
        channels = [
            channel_
                for channel_ in fetch_current_channels()
                if channel_.channel_id == key
        ]
        if len(channels) == 0:
            raise ChannelNotFound()
        return channels[0]


def fetch_current_channels():
    req = Request(INDEX_URL)
    req.add_header('User-agent', 'Macintosh')
    resp = urlopen(req)
    soup = BeautifulSoup(resp, 'lxml')
    channels_ = soup.find_all('div', class_='titles')
    channels = []
    for channel_ in channels_:
        channel = Channel.from_html(channel_)
        channels.append(channel)
    return channels
