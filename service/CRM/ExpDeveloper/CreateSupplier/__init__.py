try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSCreateSupplier import FSCreateSupplier
from .BSCreateSupplier import BSCreateSupplier
from .DSCreateSupplier import DSCreateSupplier


class CreateSupplier():
    def __init__(self):
        self.FSCreateSupplier = FSCreateSupplier
        self.BSCreateSupplier = BSCreateSupplier
        self.DSCreateSupplier = DSCreateSupplier