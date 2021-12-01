try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSNewItinerary import FSNewItinerary
from .BSNewItinerary import BSNewItinerary
from .DSNewItinerary import DSNewItinerary


class NewItinerary():
    def __init__(self):
        self.FSNewItinerary = FSNewItinerary
        self.BSNewItinerary = BSNewItinerary
        self.DSNewItinerary = DSNewItinerary