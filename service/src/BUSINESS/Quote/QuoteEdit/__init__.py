try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSQuoteEdit import FSQuoteEdit
from .BSQuoteEdit import BSQuoteEdit
from .DSQuoteEdit import DSQuoteEdit


class QuoteEdit():
    def __init__(self):
        self.FSQuoteEdit = FSQuoteEdit
        self.BSQuoteEdit = BSQuoteEdit
        self.DSQuoteEdit = DSQuoteEdit