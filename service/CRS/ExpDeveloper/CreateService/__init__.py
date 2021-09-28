try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSCreateService import FSCreateService
from .BSCreateService import BSCreateService
from .DSCreateService import DSCreateService


class CreateService():
    def __init__(self):
        self.FSCreateService = FSCreateService
        self.BSCreateService = BSCreateService
        self.DSCreateService = DSCreateService