try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSGetQuoteDetail import BSGetQuoteDetail
import logging

def FSGetQuoteDetail(uquote_id):
    try:
        result = BSGetQuoteDetail(uquote_id)
        return result

    except Exception as e:
        logging.error(e)