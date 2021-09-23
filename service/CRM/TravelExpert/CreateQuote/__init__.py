try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSCreateQuote import FSCreateQuote
from .BSCreateQuote import BSCreateQuote
from .DSCreateQuote import DSCreateQuote


class CreateQuote():
    def __init__(self):
        self.FSCreateQuote = FSCreateQuote
        self.BSCreateQuote = BSCreateQuote
        self.DSCreateQuote = DSCreateQuote