try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSFindQuote import FSFindQuote
from .BSFindQuote import BSFindQuote
from .DSFindQuote import DSFindQuote


class FindQuote():
    def __init__(self):
        self.FSFindQuote = FSFindQuote
        self.BSFindQuote = BSFindQuote
        self.DSFindQuote = DSFindQuote