try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSCancelTour import BSCancelTour
import logging

def FSCancelTour(utour_id):
    try:
        result = BSCancelTour(utour_id)
        return result

    except Exception as e:
        logging.error(e)