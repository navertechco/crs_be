try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSValidateSale import DSValidateSale
import logging

def BSValidateSale(udata):
    try:
        result = DSValidateSale(udata)
        return result

    except Exception as e:
        raise e