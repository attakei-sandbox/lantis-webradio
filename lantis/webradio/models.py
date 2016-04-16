import os
import re
from . import INDEX_URL, URL_BASE, utils, ChannelNotFound


class Channel(object):
    STREAM_HOST = 'qt.web-radio.biz:1935'

    def __init__(self, site_url, title, last_episode_url):
        self.title = title
        self.site_url = site_url
        self.last_episode_url = last_episode_url
        self.channel_id = site_url.replace(URL_BASE, '')[:-1]

    def __repr__(self):
        return self.title

    @classmethod
    def from_html(cls, dom):
        """Generate instance from BeautifulSoup object
        """
        title_ = dom.h3.a.string
        lsite_url_ = dom.h3.a.get('href')
        episode_url_ = dom.p.find_all('a')[1].get('href')
        obj = cls(lsite_url_, title_, episode_url_)
        return obj

    @classmethod
    def find(cls, key):
        channels = [
            channel_
                for channel_ in cls.fetch_current()
                if channel_.channel_id == key
        ]
        if len(channels) == 0:
            raise ChannelNotFound(key)
        return channels[0]

    @classmethod
    def fetch_current(cls):
        soup = utils.soup_url(INDEX_URL)
        channels_ = soup.find_all('div', class_='titles')
        channels = []
        for channel_ in channels_:
            channel = Channel.from_html(channel_)
            channels.append(channel)
        return channels

    def fetch_episodes(self):
        soup = utils.soup_url(self.site_url)
        episode_hrefs = [
            dom.get('href')
                for dom in soup.find_all('a')
                if self.STREAM_HOST in dom.get('href')
        ]
        episodes = []
        for url in episode_hrefs:
            parsed = Episode.parse_url(url)
            episodes.append(Episode(self, parsed['number'], url))
        return episodes


class Episode(object):
    REGEX_QT = r'mp[0-9]{1}:(?P<qt_id>.+)_(?P<number>.+)_(?P<pub_date>.+)_(?P<quality>.+).mp[0-9]{1}'

    def __init__(self, channel, number, url):
        self.channel = channel
        self.number = number
        self.url = url

    def __repr__(self):
        return '第{}回({})'.format(self.number, self.url)

    @classmethod
    def parse_url(cls, url):
        return re.search(cls.REGEX_QT, url).groupdict()

    def download(self, save_dir):
        from urllib.request import urlopen, Request
        url = self.url.replace('rtsp:', 'http:')
        url_base = os.path.dirname(url) + '/'

        # Fetch EXTM3U
        resp = utils.urlopen(url)
        m3u8_path = os.path.join(save_dir, self.channel.channel_id)
        with open(m3u8_path, 'wb') as fp:
            fp.write(resp.read())

        # Fetch playlist
        with open(m3u8_path, 'r') as fp:
            true_path = [content for content in fp.readlines() if not content.startswith('#')][0]
        true_url = url_base + true_path
        resp = utils.urlopen(true_url)
        m3u_path = os.path.join(save_dir, self.channel.channel_id + '.m3u')
        with open(m3u_path, 'wb') as fp:
            fp.write(resp.read())

        with open(m3u_path, 'r') as fp:
            index = 1
            for content in fp.readlines():
                if content.startswith('#'):
                    continue
                media_url = url_base + content
                resp = utils.urlopen(media_url)
                media_path = os.path.join(save_dir, '{}.mp3'.format(index))
                with open(media_path, 'wb') as fp:
                    fp.write(resp.read())
                index += 1
