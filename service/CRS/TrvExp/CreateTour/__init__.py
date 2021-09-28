try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSCreateTour import FSCreateTour
from .BSCreateTour import BSCreateTour
from .DSCreateTour import DSCreateTour


class CreateTour():
    def __init__(self):
        self.FSCreateTour = FSCreateTour
        self.BSCreateTour = BSCreateTour
        self.DSCreateTour = DSCreateTour