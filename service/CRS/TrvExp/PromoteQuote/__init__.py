try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSPromoteQuote import FSPromoteQuote
from .BSPromoteQuote import BSPromoteQuote
from .DSPromoteQuote import DSPromoteQuote


class PromoteQuote():
    def __init__(self):
        self.FSPromoteQuote = FSPromoteQuote
        self.BSPromoteQuote = BSPromoteQuote
        self.DSPromoteQuote = DSPromoteQuote