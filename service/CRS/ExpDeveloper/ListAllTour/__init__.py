try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSListAllTour import FSListAllTour
from .BSListAllTour import BSListAllTour
from .DSListAllTour import DSListAllTour


class ListAllTour():
    def __init__(self):
        self.FSListAllTour = FSListAllTour
        self.BSListAllTour = BSListAllTour
        self.DSListAllTour = DSListAllTour