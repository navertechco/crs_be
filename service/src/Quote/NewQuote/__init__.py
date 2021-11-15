try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSNewQuote import FSNewQuote
from .BSNewQuote import BSNewQuote
from .DSNewQuote import DSNewQuote


class NewQuote():
    def __init__(self):
        self.FSNewQuote = FSNewQuote
        self.BSNewQuote = BSNewQuote
        self.DSNewQuote = DSNewQuote