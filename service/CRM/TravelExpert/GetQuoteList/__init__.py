try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSGetQuoteList import FSGetQuoteList
from .BSGetQuoteList import BSGetQuoteList
from .DSGetQuoteList import DSGetQuoteList


class GetQuoteList():
    def __init__(self):
        self.FSGetQuoteList = FSGetQuoteList
        self.BSGetQuoteList = BSGetQuoteList
        self.DSGetQuoteList = DSGetQuoteList