try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSListAllSale import FSListAllSale
from .BSListAllSale import BSListAllSale
from .DSListAllSale import DSListAllSale


class ListAllSale():
    def __init__(self):
        self.FSListAllSale = FSListAllSale
        self.BSListAllSale = BSListAllSale
        self.DSListAllSale = DSListAllSale