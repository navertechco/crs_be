try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSReset import BSReset
import logging

def FSReset(uusername):
    try:
        result = BSReset(uusername)
        return result

    except Exception as e:
        logging.error(e)