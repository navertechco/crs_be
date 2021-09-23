try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSGetActivityList import FSGetActivityList
from .BSGetActivityList import BSGetActivityList
from .DSGetActivityList import DSGetActivityList


class GetActivityList():
    def __init__(self):
        self.FSGetActivityList = FSGetActivityList
        self.BSGetActivityList = BSGetActivityList
        self.DSGetActivityList = DSGetActivityList