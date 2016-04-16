import sys
from .abstract import AbstractCommand
from ..models import Channel


class ListCommand(AbstractCommand):
    def run(self, out=sys.stdout, err=sys.stderr):
        for channel in Channel.fetch_current():
            out.write(channel.channel_id + ' :\n')
            out.write('\t' + channel.title + '\n')
