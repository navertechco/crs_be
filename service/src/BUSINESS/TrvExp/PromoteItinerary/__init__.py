try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSPromoteItinerary import FSPromoteItinerary
from .BSPromoteItinerary import BSPromoteItinerary
from .DSPromoteItinerary import DSPromoteItinerary


class PromoteItinerary():
    def __init__(self):
        self.FSPromoteItinerary = FSPromoteItinerary
        self.BSPromoteItinerary = BSPromoteItinerary
        self.DSPromoteItinerary = DSPromoteItinerary