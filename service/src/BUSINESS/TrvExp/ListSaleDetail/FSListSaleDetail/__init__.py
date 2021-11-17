try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSListSaleDetail import BSListSaleDetail
import logging

def FSListSaleDetail(udata):
    try:
        result = BSListSaleDetail(udata)
        return result

    except Exception as e:
        logging.error(e)