try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSCancelItinerary import FSCancelItinerary
from .BSCancelItinerary import BSCancelItinerary
from .DSCancelItinerary import DSCancelItinerary


class CancelItinerary():
    def __init__(self):
        self.FSCancelItinerary = FSCancelItinerary
        self.BSCancelItinerary = BSCancelItinerary
        self.DSCancelItinerary = DSCancelItinerary