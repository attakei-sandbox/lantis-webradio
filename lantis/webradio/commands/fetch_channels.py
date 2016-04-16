# -*- coding:utf8 -*-
from .. import INDEX_URL, Channel


def main():
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
