try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSGetSupplierList import FSGetSupplierList
from .BSGetSupplierList import BSGetSupplierList
from .DSGetSupplierList import DSGetSupplierList


class GetSupplierList():
    def __init__(self):
        self.FSGetSupplierList = FSGetSupplierList
        self.BSGetSupplierList = BSGetSupplierList
        self.DSGetSupplierList = DSGetSupplierList