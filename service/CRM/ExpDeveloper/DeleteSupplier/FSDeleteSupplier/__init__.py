try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSDeleteSupplier import BSDeleteSupplier
import logging

def FSDeleteSupplier(usupplier_id):
    try:
        result = BSDeleteSupplier(usupplier_id)
        return result

    except Exception as e:
        logging.error(e)