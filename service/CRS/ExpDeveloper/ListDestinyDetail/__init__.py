try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSListDestinyDetail import FSListDestinyDetail
from .BSListDestinyDetail import BSListDestinyDetail
from .DSListDestinyDetail import DSListDestinyDetail


class ListDestinyDetail():
    def __init__(self):
        self.FSListDestinyDetail = FSListDestinyDetail
        self.BSListDestinyDetail = BSListDestinyDetail
        self.DSListDestinyDetail = DSListDestinyDetail