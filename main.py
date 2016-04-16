#!/usr/bin/env python
# -*- coding:utf8 -*-
import sys
import argparse


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



parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

parser_list = subparsers.add_parser('list')
parser_list.set_defaults(func=fetch_channels)


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    args = parser.parse_args()
    args.func()


if __name__ == '__main__':
    main()
