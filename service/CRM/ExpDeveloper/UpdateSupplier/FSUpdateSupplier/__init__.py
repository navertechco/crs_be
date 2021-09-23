try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSUpdateSupplier import BSUpdateSupplier
import logging

def FSUpdateSupplier(udata):
    try:
        result = BSUpdateSupplier(udata)
        return result

    except Exception as e:
        logging.error(e)