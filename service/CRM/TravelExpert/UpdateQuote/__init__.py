try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSUpdateQuote import FSUpdateQuote
from .BSUpdateQuote import BSUpdateQuote
from .DSUpdateQuote import DSUpdateQuote


class UpdateQuote():
    def __init__(self):
        self.FSUpdateQuote = FSUpdateQuote
        self.BSUpdateQuote = BSUpdateQuote
        self.DSUpdateQuote = DSUpdateQuote