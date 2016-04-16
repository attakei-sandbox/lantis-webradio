import sys
from .. import Channel, ChannelNotFound
from .abstract import AbstractCommand


class DetailCommand(AbstractCommand):
    @classmethod
    def configure_parser(cls, parser):
        parser.add_argument('channel', help='channnel key')

    def run(self, out=sys.stdout, err=sys.stderr):
        channnel_key = self.args.channel
        try:
            channel = Channel.find(channnel_key)
        except ChannelNotFound:
            err.write('Channel "{}" is not found.\n'.format(channnel_key))
            return
        out.write('Hello! I am "{}"\n'.format(channel.title))
