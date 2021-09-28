try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSListMediaDetail import FSListMediaDetail
from .BSListMediaDetail import BSListMediaDetail
from .DSListMediaDetail import DSListMediaDetail


class ListMediaDetail():
    def __init__(self):
        self.FSListMediaDetail = FSListMediaDetail
        self.BSListMediaDetail = BSListMediaDetail
        self.DSListMediaDetail = DSListMediaDetail