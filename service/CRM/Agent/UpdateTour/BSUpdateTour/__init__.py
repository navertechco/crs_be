try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSUpdateTour import DSUpdateTour
import logging

def BSUpdateTour(udata):
    try:
        result = DSUpdateTour(udata)
        return result

    except Exception as e:
        logging.error(e)