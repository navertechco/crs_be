try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSValidateProspect import DSValidateProspect
import logging

def BSValidateProspect(udata):
    try:
        result = DSValidateProspect(udata)
        return result

    except Exception as e:
        logging.error(e)