try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSCreateSale import FSCreateSale
from .BSCreateSale import BSCreateSale
from .DSCreateSale import DSCreateSale


class CreateSale():
    def __init__(self):
        self.FSCreateSale = FSCreateSale
        self.BSCreateSale = BSCreateSale
        self.DSCreateSale = DSCreateSale