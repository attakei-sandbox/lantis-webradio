import sys
from .abstract import AbstractCommand
from .. import ChannelNotFound
from ..models import Channel


class EpisodeListCommand(AbstractCommand):
    @classmethod
    def configure_parser(cls, parser):
        parser.add_argument('channel', help='channnel key')

    def run(self, out=sys.stdout, err=sys.stderr):
        channnel_key = self.args.channel
        try:
            channel = Channel.find(channnel_key)
        except ChannelNotFound as ex:
            err.write(str(ex) + '\n')
            return 1
        episodes = channel.fetch_episodes()
        for episode in episodes:
            out.write(str(episode) + '\n')

    def out_detail_information(self, channel, out):
        description = 'Descriontion:\n' \
            '    Title:       {title}\n' \
            '    Site:        {site_url}\n' \
            '    LastEpisode: {last_episode_url}\n'
        out.write(description.format(**channel.__dict__))
