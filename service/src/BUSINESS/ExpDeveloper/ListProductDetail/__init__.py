try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSListProductDetail import FSListProductDetail
from .BSListProductDetail import BSListProductDetail
from .DSListProductDetail import DSListProductDetail


class ListProductDetail():
    def __init__(self):
        self.FSListProductDetail = FSListProductDetail
        self.BSListProductDetail = BSListProductDetail
        self.DSListProductDetail = DSListProductDetail