try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSUpdateItinerary import FSUpdateItinerary
from .BSUpdateItinerary import BSUpdateItinerary
from .DSUpdateItinerary import DSUpdateItinerary


class UpdateItinerary():
    def __init__(self):
        self.FSUpdateItinerary = FSUpdateItinerary
        self.BSUpdateItinerary = BSUpdateItinerary
        self.DSUpdateItinerary = DSUpdateItinerary