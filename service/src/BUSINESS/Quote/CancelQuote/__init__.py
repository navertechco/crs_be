try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSCancelQuote import FSCancelQuote
from .BSCancelQuote import BSCancelQuote
from .DSCancelQuote import DSCancelQuote


class CancelQuote():
    def __init__(self):
        self.FSCancelQuote = FSCancelQuote
        self.BSCancelQuote = BSCancelQuote
        self.DSCancelQuote = DSCancelQuote