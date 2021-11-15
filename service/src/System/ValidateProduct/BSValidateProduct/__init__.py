try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSValidateProduct import DSValidateProduct
import logging

def BSValidateProduct(udata):
    try:
        result = DSValidateProduct(udata)
        return result

    except Exception as e:
        logging.error(e)