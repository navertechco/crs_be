try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSDeleteTour import DSDeleteTour
import logging

def BSDeleteTour(utour_id):
    try:
        result = DSDeleteTour(utour_id)
        return result

    except Exception as e:
        logging.error(e)