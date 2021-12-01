try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSItineraryEdit import FSItineraryEdit
from .BSItineraryEdit import BSItineraryEdit
from .DSItineraryEdit import DSItineraryEdit


class ItineraryEdit():
    def __init__(self):
        self.FSItineraryEdit = FSItineraryEdit
        self.BSItineraryEdit = BSItineraryEdit
        self.DSItineraryEdit = DSItineraryEdit