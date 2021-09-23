try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSUpdateSupplier import FSUpdateSupplier
from .BSUpdateSupplier import BSUpdateSupplier
from .DSUpdateSupplier import DSUpdateSupplier


class UpdateSupplier():
    def __init__(self):
        self.FSUpdateSupplier = FSUpdateSupplier
        self.BSUpdateSupplier = BSUpdateSupplier
        self.DSUpdateSupplier = DSUpdateSupplier