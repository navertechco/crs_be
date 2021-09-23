try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSGetDestinyDetail import FSGetDestinyDetail
from .BSGetDestinyDetail import BSGetDestinyDetail
from .DSGetDestinyDetail import DSGetDestinyDetail


class GetDestinyDetail():
    def __init__(self):
        self.FSGetDestinyDetail = FSGetDestinyDetail
        self.BSGetDestinyDetail = BSGetDestinyDetail
        self.DSGetDestinyDetail = DSGetDestinyDetail