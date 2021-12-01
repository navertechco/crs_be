try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSLogItinerary import DSLogItinerary
import logging

def BSLogItinerary(udata):
    try:
        result = DSLogItinerary(udata)
        return result

    except Exception as e:
        logging.error(e)