try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSGetPollList import FSGetPollList
from .BSGetPollList import BSGetPollList
from .DSGetPollList import DSGetPollList


class GetPollList():
    def __init__(self):
        self.FSGetPollList = FSGetPollList
        self.BSGetPollList = BSGetPollList
        self.DSGetPollList = DSGetPollList