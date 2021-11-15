try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSProccessQuote import FSProccessQuote
from .BSProccessQuote import BSProccessQuote
from .DSProccessQuote import DSProccessQuote


class ProccessQuote():
    def __init__(self):
        self.FSProccessQuote = FSProccessQuote
        self.BSProccessQuote = BSProccessQuote
        self.DSProccessQuote = DSProccessQuote