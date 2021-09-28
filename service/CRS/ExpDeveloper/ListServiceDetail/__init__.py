try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSListServiceDetail import FSListServiceDetail
from .BSListServiceDetail import BSListServiceDetail
from .DSListServiceDetail import DSListServiceDetail


class ListServiceDetail():
    def __init__(self):
        self.FSListServiceDetail = FSListServiceDetail
        self.BSListServiceDetail = BSListServiceDetail
        self.DSListServiceDetail = DSListServiceDetail