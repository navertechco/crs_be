try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSUpdateUpSelling import DSUpdateUpSelling
import logging

def BSUpdateUpSelling(udata):
    try:
        result = DSUpdateUpSelling(udata)
        return result

    except Exception as e:
        logging.error(e)