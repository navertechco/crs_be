try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSListAllSupplier import FSListAllSupplier
from .BSListAllSupplier import BSListAllSupplier
from .DSListAllSupplier import DSListAllSupplier


class ListAllSupplier():
    def __init__(self):
        self.FSListAllSupplier = FSListAllSupplier
        self.BSListAllSupplier = BSListAllSupplier
        self.DSListAllSupplier = DSListAllSupplier