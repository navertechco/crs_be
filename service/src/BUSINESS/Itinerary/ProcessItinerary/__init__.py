try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSProcessItinerary import FSProcessItinerary
from .BSProcessItinerary import BSProcessItinerary
from .DSProcessItinerary import DSProcessItinerary


class ProcessItinerary():
    def __init__(self):
        self.FSProcessItinerary = FSProcessItinerary
        self.BSProcessItinerary = BSProcessItinerary
        self.DSProcessItinerary = DSProcessItinerary