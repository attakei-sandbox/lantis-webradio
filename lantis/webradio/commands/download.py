import sys
import shutil
from mutagen import id3
from .abstract import AbstractCommand
from .. import ChannelNotFound, settings
from ..models import Channel


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
        fullpath = episode.download('/var/lib/lantis/tmp')

        # Edit tag
        audio_tags = id3.ID3(fullpath)
        audio_tags.add(id3.TIT2(encoding=3, text='{} 第{}回'.format(channel.title, episode.number)))
        audio_tags.add(id3.TALB(encoding=3, text=channel.title))
        audio_tags.add(id3.TRK(encoding=3, text=episode.number))
        audio_tags.save()

        # Save
        if settings.SAVE_STORAGE == 'local':
            shutil.copy(fullpath, settings.SAVE_STORAGE_PATH)
