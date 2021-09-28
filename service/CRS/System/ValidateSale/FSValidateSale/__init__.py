try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSValidateSale import BSValidateSale
import logging

def FSValidateSale(udata):
    try:
        result = BSValidateSale(udata)
        return result

    except Exception as e:
        logging.error(e)