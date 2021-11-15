try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSEditSale import FSEditSale
from .BSEditSale import BSEditSale
from .DSEditSale import DSEditSale


class EditSale():
    def __init__(self):
        self.FSEditSale = FSEditSale
        self.BSEditSale = BSEditSale
        self.DSEditSale = DSEditSale