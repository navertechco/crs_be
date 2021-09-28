try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSEditService import FSEditService
from .BSEditService import BSEditService
from .DSEditService import DSEditService


class EditService():
    def __init__(self):
        self.FSEditService = FSEditService
        self.BSEditService = BSEditService
        self.DSEditService = DSEditService