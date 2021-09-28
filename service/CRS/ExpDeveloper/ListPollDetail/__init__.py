try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSListPollDetail import FSListPollDetail
from .BSListPollDetail import BSListPollDetail
from .DSListPollDetail import DSListPollDetail


class ListPollDetail():
    def __init__(self):
        self.FSListPollDetail = FSListPollDetail
        self.BSListPollDetail = BSListPollDetail
        self.DSListPollDetail = DSListPollDetail