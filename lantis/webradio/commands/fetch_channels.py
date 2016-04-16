# -*- coding:utf8 -*-
import sys
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from .. import INDEX_URL, Channel


def main(out=sys.stdout, err=sys.stderr):
    """Fetch current chennels in lantis-net.com
    """
    req = Request(INDEX_URL)
    req.add_header('User-agent', 'Macintosh')
    resp = urlopen(req)
    soup = BeautifulSoup(resp, 'lxml')
    channels = soup.find_all('div', class_='titles')
    for channel_ in channels:
        channel = Channel.from_html(channel_)
        out.write(channel.channel_id + ' :\n')
        out.write('\t' + channel.title + '\n')
