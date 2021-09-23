try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSFindQuote import BSFindQuote
import logging

def FSFindQuote(uquote_id, uprops):
    try:
        result = BSFindQuote(uquote_id, uprops)
        return result

    except Exception as e:
        logging.error(e)