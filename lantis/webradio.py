# -*- coding:utf8 -*-


INDEX_URL = 'http://lantis-net.com/index.html'


def fetch_channels():
    """Fetch current chennels in lantis-net.com
    """
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    resp = urlopen(INDEX_URL)
    soup = BeautifulSoup(resp, 'lxml')
    channels = soup.find_all('div', class_='titles')
    for channel in channels:
        print(channel.h3.a.string)
