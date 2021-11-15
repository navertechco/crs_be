try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSListAllCatalogue import FSListAllCatalogue
from .BSListAllCatalogue import BSListAllCatalogue
from .DSListAllCatalogue import DSListAllCatalogue


class ListAllCatalogue():
    def __init__(self):
        self.FSListAllCatalogue = FSListAllCatalogue
        self.BSListAllCatalogue = BSListAllCatalogue
        self.DSListAllCatalogue = DSListAllCatalogue