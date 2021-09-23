try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSGetTourDetail import FSGetTourDetail
from .BSGetTourDetail import BSGetTourDetail
from .DSGetTourDetail import DSGetTourDetail


class GetTourDetail():
    def __init__(self):
        self.FSGetTourDetail = FSGetTourDetail
        self.BSGetTourDetail = BSGetTourDetail
        self.DSGetTourDetail = DSGetTourDetail