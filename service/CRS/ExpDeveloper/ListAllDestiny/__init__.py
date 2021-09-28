try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSListAllDestiny import FSListAllDestiny
from .BSListAllDestiny import BSListAllDestiny
from .DSListAllDestiny import DSListAllDestiny


class ListAllDestiny():
    def __init__(self):
        self.FSListAllDestiny = FSListAllDestiny
        self.BSListAllDestiny = BSListAllDestiny
        self.DSListAllDestiny = DSListAllDestiny