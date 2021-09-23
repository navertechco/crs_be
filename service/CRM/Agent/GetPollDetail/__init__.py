try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSGetPollDetail import FSGetPollDetail
from .BSGetPollDetail import BSGetPollDetail
from .DSGetPollDetail import DSGetPollDetail


class GetPollDetail():
    def __init__(self):
        self.FSGetPollDetail = FSGetPollDetail
        self.BSGetPollDetail = BSGetPollDetail
        self.DSGetPollDetail = DSGetPollDetail