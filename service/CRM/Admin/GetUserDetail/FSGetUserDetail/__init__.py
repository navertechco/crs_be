try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSGetUserDetail import BSGetUserDetail
import logging

def FSGetUserDetail(uuser_id):
    try:
        result = BSGetUserDetail(uuser_id)
        return result

    except Exception as e:
        logging.error(e)