import sys


class AbstractCommand(object):
    def __init__(self, args):
        self.args = args

    @classmethod
    def configure_parser(cls, parser):
        pass

    def run(self, out=sys.stdout, err=sys.stderr):
        raise NotImplemented()
