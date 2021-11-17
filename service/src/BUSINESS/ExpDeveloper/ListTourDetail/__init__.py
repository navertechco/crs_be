try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSListTourDetail import FSListTourDetail
from .BSListTourDetail import BSListTourDetail
from .DSListTourDetail import DSListTourDetail


class ListTourDetail():
    def __init__(self):
        self.FSListTourDetail = FSListTourDetail
        self.BSListTourDetail = BSListTourDetail
        self.DSListTourDetail = DSListTourDetail