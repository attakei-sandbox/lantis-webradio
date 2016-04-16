from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


def soup_url(url):
    req = Request(url)
    req.add_header('User-agent', 'Macintosh')
    resp = urlopen(req)
    return BeautifulSoup(resp, 'lxml')
