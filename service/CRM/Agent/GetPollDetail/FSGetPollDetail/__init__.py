try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSGetPollDetail import BSGetPollDetail
import logging

def FSGetPollDetail(upoll_id):
    try:
        result = BSGetPollDetail(upoll_id)
        return result

    except Exception as e:
        logging.error(e)