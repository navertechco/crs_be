try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSDeleteQuote import BSDeleteQuote
import logging

def FSDeleteQuote(uquote_id):
    try:
        result = BSDeleteQuote(uquote_id)
        return result

    except Exception as e:
        logging.error(e)