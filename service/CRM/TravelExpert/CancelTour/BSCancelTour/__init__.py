try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSCancelTour import DSCancelTour
import logging

def BSCancelTour(utour_id):
    try:
        result = DSCancelTour(utour_id)
        return result

    except Exception as e:
        logging.error(e)