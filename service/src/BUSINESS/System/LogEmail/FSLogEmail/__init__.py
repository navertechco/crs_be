try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSLogEmail import BSLogEmail
import logging

def FSLogEmail(udata):
    try:
        result = BSLogEmail(udata)
        return result

    except Exception as e:
        logging.error(e)