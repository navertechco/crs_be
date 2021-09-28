try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSValidateTour import DSValidateTour
import logging

def BSValidateTour(udata):
    try:
        result = DSValidateTour(udata)
        return result

    except Exception as e:
        logging.error(e)