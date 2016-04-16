# -*- coding:utf8 -*-
import sys
from .list import ListCommand
from .detail import DetailCommand


ALL_COMMANDS = {
    'list' : ListCommand,
    'detail': DetailCommand,
}



def bind_subparsers(subparsers):
    for cmd, Command in ALL_COMMANDS.items():
        parser = subparsers.add_parser(cmd)
        parser.set_defaults(Command=Command)
        Command.configure_parser(parser)
