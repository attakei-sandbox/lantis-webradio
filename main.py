#!/usr/bin/env python
# -*- coding:utf8 -*-
import sys
import argparse
from lantis.webradio.commands import (
    fetch_channels,
    detail_channel,
)


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

parser_list = subparsers.add_parser('list')
parser_list.set_defaults(func=fetch_channels)

parser_detail = subparsers.add_parser('detail')
parser_detail.set_defaults(func=detail_channel)
parser_detail.add_argument('channel', help='channnel key')


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    args = parser.parse_args()
    args.func.main(args)


if __name__ == '__main__':
    main()
