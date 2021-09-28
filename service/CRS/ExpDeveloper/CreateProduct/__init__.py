try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSCreateProduct import FSCreateProduct
from .BSCreateProduct import BSCreateProduct
from .DSCreateProduct import DSCreateProduct


class CreateProduct():
    def __init__(self):
        self.FSCreateProduct = FSCreateProduct
        self.BSCreateProduct = BSCreateProduct
        self.DSCreateProduct = DSCreateProduct