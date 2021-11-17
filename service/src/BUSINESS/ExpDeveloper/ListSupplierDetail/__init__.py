try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSListSupplierDetail import FSListSupplierDetail
from .BSListSupplierDetail import BSListSupplierDetail
from .DSListSupplierDetail import DSListSupplierDetail


class ListSupplierDetail():
    def __init__(self):
        self.FSListSupplierDetail = FSListSupplierDetail
        self.BSListSupplierDetail = BSListSupplierDetail
        self.DSListSupplierDetail = DSListSupplierDetail