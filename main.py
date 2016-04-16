#!/usr/bin/env python
# -*- coding:utf8 -*-
import sys
import argparse
from lantis.webradio import fetch_channels


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
