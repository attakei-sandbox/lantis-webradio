from urllib.request import urlopen as urlopen_origin
from urllib.request import Request
from bs4 import BeautifulSoup


def urlopen(url):
    req = Request(url)
    req.add_header('User-agent', 'Macintosh; Intel Mac OS X 10_11_4')
    return urlopen_origin(req)


def soup_url(url):
    resp = urlopen(url)
    return BeautifulSoup(resp, 'lxml')
