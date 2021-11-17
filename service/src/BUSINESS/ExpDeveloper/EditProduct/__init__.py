try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSEditProduct import FSEditProduct
from .BSEditProduct import BSEditProduct
from .DSEditProduct import DSEditProduct


class EditProduct():
    def __init__(self):
        self.FSEditProduct = FSEditProduct
        self.BSEditProduct = BSEditProduct
        self.DSEditProduct = DSEditProduct