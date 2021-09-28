try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSListSaleDetail import FSListSaleDetail
from .BSListSaleDetail import BSListSaleDetail
from .DSListSaleDetail import DSListSaleDetail


class ListSaleDetail():
    def __init__(self):
        self.FSListSaleDetail = FSListSaleDetail
        self.BSListSaleDetail = BSListSaleDetail
        self.DSListSaleDetail = DSListSaleDetail