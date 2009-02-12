from opml import *

try:
    __version__ = __import__('pkg_resources').get_distribution('OPML_Parser').version
except:
    __version__ = '?'
