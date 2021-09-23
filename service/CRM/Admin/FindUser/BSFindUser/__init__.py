try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSFindUser import DSFindUser
import logging

def BSFindUser(uuser_id, uprops):
    try:
        result = DSFindUser(uuser_id, uprops)
        return result

    except Exception as e:
        logging.error(e)