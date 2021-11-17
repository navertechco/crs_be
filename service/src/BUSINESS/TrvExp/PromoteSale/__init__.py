try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSPromoteSale import FSPromoteSale
from .BSPromoteSale import BSPromoteSale
from .DSPromoteSale import DSPromoteSale


class PromoteSale():
    def __init__(self):
        self.FSPromoteSale = FSPromoteSale
        self.BSPromoteSale = BSPromoteSale
        self.DSPromoteSale = DSPromoteSale