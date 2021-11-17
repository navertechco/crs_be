try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSListDestinyDetail import DSListDestinyDetail
import logging

def BSListDestinyDetail(udata):
    try:
        result = DSListDestinyDetail(udata)
        return result

    except Exception as e:
        logging.error(e)