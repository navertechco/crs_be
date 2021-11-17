try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSListAllProduct import FSListAllProduct
from .BSListAllProduct import BSListAllProduct
from .DSListAllProduct import DSListAllProduct


class ListAllProduct():
    def __init__(self):
        self.FSListAllProduct = FSListAllProduct
        self.BSListAllProduct = BSListAllProduct
        self.DSListAllProduct = DSListAllProduct