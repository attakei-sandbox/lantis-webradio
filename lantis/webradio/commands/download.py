import sys
from .abstract import AbstractCommand
from ..models import Channel
from .. import ChannelNotFound


class DownloadCommand(AbstractCommand):
    @classmethod
    def configure_parser(cls, parser):
        parser.add_argument('channel', help='channnel key')
        parser.add_argument('number', help='episode number')

    def run(self, out=sys.stdout, err=sys.stderr):
        channnel_key = self.args.channel
        episode_number = self.args.number
        episode = None
        try:
            channel = Channel.find(channnel_key)
            episodes = channel.fetch_episodes()
            for episode_ in episodes:
                if episode_.number == episode_number:
                    episode = episode_
                    break
            else:
                raise ChannelNotFound('xxx')
        except ChannelNotFound as ex:
            err.write(str(ex) + '\n')
            return 1
        episode.download('/var/lib/lantis/tmp')
