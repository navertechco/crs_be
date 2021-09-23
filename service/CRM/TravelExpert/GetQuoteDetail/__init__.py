try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSGetQuoteDetail import FSGetQuoteDetail
from .BSGetQuoteDetail import BSGetQuoteDetail
from .DSGetQuoteDetail import DSGetQuoteDetail


class GetQuoteDetail():
    def __init__(self):
        self.FSGetQuoteDetail = FSGetQuoteDetail
        self.BSGetQuoteDetail = BSGetQuoteDetail
        self.DSGetQuoteDetail = DSGetQuoteDetail