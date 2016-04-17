import os

URL_BASE = 'http://lantis-net.com/'


INDEX_URL = 'http://lantis-net.com/index.html'


SAVE_STORAGE = os.environ.get('SAVE_STORAGE', 'local')
SAVE_STORAGE_PATH = os.environ.get('SAVE_STORAGE_PATH', '/var/lib/lantis/data')
