try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSFindQuote import DSFindQuote
import logging

def BSFindQuote(uquote_id, uprops):
    try:
        result = DSFindQuote(uquote_id, uprops)
        return result

    except Exception as e:
        logging.error(e)