try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSEditSupplier import FSEditSupplier
from .BSEditSupplier import BSEditSupplier
from .DSEditSupplier import DSEditSupplier


class EditSupplier():
    def __init__(self):
        self.FSEditSupplier = FSEditSupplier
        self.BSEditSupplier = BSEditSupplier
        self.DSEditSupplier = DSEditSupplier