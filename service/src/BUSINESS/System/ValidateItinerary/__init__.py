try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSValidateItinerary import FSValidateItinerary
from .BSValidateItinerary import BSValidateItinerary
from .DSValidateItinerary import DSValidateItinerary


class ValidateItinerary():
    def __init__(self):
        self.FSValidateItinerary = FSValidateItinerary
        self.BSValidateItinerary = BSValidateItinerary
        self.DSValidateItinerary = DSValidateItinerary