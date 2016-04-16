# -*- coding:utf8 -*-


URL_BASE = 'http://lantis-net.com/'
INDEX_URL = 'http://lantis-net.com/index.html'


def fetch_channels():
    """Fetch current chennels in lantis-net.com
    """
    from urllib.request import urlopen, Request
    from bs4 import BeautifulSoup
    req = Request(INDEX_URL)
    req.add_header('User-agent', 'Macintosh')
    resp = urlopen(req)
    soup = BeautifulSoup(resp, 'lxml')
    channels = soup.find_all('div', class_='titles')
    for channel_ in channels:
        channel = Channel.from_html(channel_)
        print(channel.channel_id, ':')
        print('\t', channel.title)


class Channel(object):
    def __init__(self, site_url, title, latest_episode_url):
        self.title = title
        self.site_url = site_url
        self.latest_episode_url = latest_episode_url
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
