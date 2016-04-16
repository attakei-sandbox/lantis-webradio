import sys
from .. import ChannelNotFound
from ..models import Channel
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
        self.out_detail_information(channel, out)

    def out_detail_information(self, channel, out):
        description = 'Descriontion:\n' \
            '    Title:       {title}\n' \
            '    Site:        {site_url}\n' \
            '    LastEpisode: {last_episode_url}\n'
        out.write(description.format(**channel.__dict__))
