#!/usr/bin/env python
# -*- coding:utf8 -*-
import sys
import argparse
from lantis.webradio.commands import bind_subparsers


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()
bind_subparsers(subparsers)


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    args = parser.parse_args()
    command = args.Command(args)
    command.run()


if __name__ == '__main__':
    main()
