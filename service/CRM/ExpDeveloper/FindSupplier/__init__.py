try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSFindSupplier import FSFindSupplier
from .BSFindSupplier import BSFindSupplier
from .DSFindSupplier import DSFindSupplier


class FindSupplier():
    def __init__(self):
        self.FSFindSupplier = FSFindSupplier
        self.BSFindSupplier = BSFindSupplier
        self.DSFindSupplier = DSFindSupplier