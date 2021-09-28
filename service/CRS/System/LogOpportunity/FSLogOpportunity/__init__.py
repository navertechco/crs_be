try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSLogOpportunity import BSLogOpportunity
import logging

def FSLogOpportunity(udata):
    try:
        result = BSLogOpportunity(udata)
        return result

    except Exception as e:
        logging.error(e)