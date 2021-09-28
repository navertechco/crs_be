try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSEditTour import FSEditTour
from .BSEditTour import BSEditTour
from .DSEditTour import DSEditTour


class EditTour():
    def __init__(self):
        self.FSEditTour = FSEditTour
        self.BSEditTour = BSEditTour
        self.DSEditTour = DSEditTour