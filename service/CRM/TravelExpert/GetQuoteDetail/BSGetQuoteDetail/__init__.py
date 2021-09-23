try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSGetQuoteDetail import DSGetQuoteDetail
import logging

def BSGetQuoteDetail(uquote_id):
    try:
        result = DSGetQuoteDetail(uquote_id)
        return result

    except Exception as e:
        logging.error(e)