try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSPromoteItinerary import DSPromoteItinerary
import logging

def BSPromoteItinerary(udata):
    try:
        result = DSPromoteItinerary(udata)
        return result

    except Exception as e:
        logging.error(e)