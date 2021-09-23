try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSGetVideoList import FSGetVideoList
from .BSGetVideoList import BSGetVideoList
from .DSGetVideoList import DSGetVideoList


class GetVideoList():
    def __init__(self):
        self.FSGetVideoList = FSGetVideoList
        self.BSGetVideoList = BSGetVideoList
        self.DSGetVideoList = DSGetVideoList