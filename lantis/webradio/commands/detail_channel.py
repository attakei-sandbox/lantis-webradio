# -*- coding:utf8 -*-
import sys
from .. import INDEX_URL, Channel, ChannelNotFound



def main(args, out=sys.stdout, err=sys.stderr):
    """Fetch current chennels in lantis-net.com
    """
    try:
        channel = Channel.find(args.channel)
    except ChannelNotFound:
        err.write('Channel "{}" is not found.\n'.format(args.channel))
        return
    out.write('Hello! I am "{}"\n'.format(channel.title))
