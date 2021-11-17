try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSListAllService import FSListAllService
from .BSListAllService import BSListAllService
from .DSListAllService import DSListAllService


class ListAllService():
    def __init__(self):
        self.FSListAllService = FSListAllService
        self.BSListAllService = BSListAllService
        self.DSListAllService = DSListAllService