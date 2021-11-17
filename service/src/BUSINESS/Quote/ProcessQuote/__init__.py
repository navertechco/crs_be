try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSProcessQuote import FSProcessQuote
from .BSProcessQuote import BSProcessQuote
from .DSProcessQuote import DSProcessQuote


class ProcessQuote():
    def __init__(self):
        self.FSProcessQuote = FSProcessQuote
        self.BSProcessQuote = BSProcessQuote
        self.DSProcessQuote = DSProcessQuote