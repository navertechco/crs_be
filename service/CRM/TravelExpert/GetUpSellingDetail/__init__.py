try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSGetUpSellingDetail import FSGetUpSellingDetail
from .BSGetUpSellingDetail import BSGetUpSellingDetail
from .DSGetUpSellingDetail import DSGetUpSellingDetail


class GetUpSellingDetail():
    def __init__(self):
        self.FSGetUpSellingDetail = FSGetUpSellingDetail
        self.BSGetUpSellingDetail = BSGetUpSellingDetail
        self.DSGetUpSellingDetail = DSGetUpSellingDetail