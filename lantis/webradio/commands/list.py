import sys
from .. import fetch_current_channels
from .abstract import AbstractCommand


class ListCommand(AbstractCommand):
    def run(self, out=sys.stdout, err=sys.stderr):
        for channel in fetch_current_channels():
            out.write(channel.channel_id + ' :\n')
            out.write('\t' + channel.title + '\n')
