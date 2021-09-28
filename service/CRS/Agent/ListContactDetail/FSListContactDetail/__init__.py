try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSListContactDetail import BSListContactDetail
import logging

def FSListContactDetail(udata):
    try:
        result = BSListContactDetail(udata)
        return result

    except Exception as e:
        logging.error(e)