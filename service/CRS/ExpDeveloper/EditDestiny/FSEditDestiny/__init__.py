try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSEditDestiny import BSEditDestiny
import logging

def FSEditDestiny(udata):
    try:
        result = BSEditDestiny(udata)
        return result

    except Exception as e:
        logging.error(e)