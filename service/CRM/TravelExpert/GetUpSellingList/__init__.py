try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSGetUpSellingList import FSGetUpSellingList
from .BSGetUpSellingList import BSGetUpSellingList
from .DSGetUpSellingList import DSGetUpSellingList


class GetUpSellingList():
    def __init__(self):
        self.FSGetUpSellingList = FSGetUpSellingList
        self.BSGetUpSellingList = BSGetUpSellingList
        self.DSGetUpSellingList = DSGetUpSellingList