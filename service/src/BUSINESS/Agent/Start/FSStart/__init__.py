try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSStart import BSStart
import logging

def FSStart(udata):
    try:
        result = BSStart(udata)
        return result

    except Exception as e:
        logging.error(e)