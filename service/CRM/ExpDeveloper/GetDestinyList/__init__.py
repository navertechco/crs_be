try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSGetDestinyList import FSGetDestinyList
from .BSGetDestinyList import BSGetDestinyList
from .DSGetDestinyList import DSGetDestinyList


class GetDestinyList():
    def __init__(self):
        self.FSGetDestinyList = FSGetDestinyList
        self.BSGetDestinyList = BSGetDestinyList
        self.DSGetDestinyList = DSGetDestinyList