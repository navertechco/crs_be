try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSDeleteQuote import FSDeleteQuote
from .BSDeleteQuote import BSDeleteQuote
from .DSDeleteQuote import DSDeleteQuote


class DeleteQuote():
    def __init__(self):
        self.FSDeleteQuote = FSDeleteQuote
        self.BSDeleteQuote = BSDeleteQuote
        self.DSDeleteQuote = DSDeleteQuote