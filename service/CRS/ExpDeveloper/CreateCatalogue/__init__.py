try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSCreateCatalogue import FSCreateCatalogue
from .BSCreateCatalogue import BSCreateCatalogue
from .DSCreateCatalogue import DSCreateCatalogue


class CreateCatalogue():
    def __init__(self):
        self.FSCreateCatalogue = FSCreateCatalogue
        self.BSCreateCatalogue = BSCreateCatalogue
        self.DSCreateCatalogue = DSCreateCatalogue