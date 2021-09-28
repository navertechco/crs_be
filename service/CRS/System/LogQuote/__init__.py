try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSLogQuote import FSLogQuote
from .BSLogQuote import BSLogQuote
from .DSLogQuote import DSLogQuote


class LogQuote():
    def __init__(self):
        self.FSLogQuote = FSLogQuote
        self.BSLogQuote = BSLogQuote
        self.DSLogQuote = DSLogQuote