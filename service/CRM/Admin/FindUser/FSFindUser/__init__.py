try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSFindUser import BSFindUser
import logging

def FSFindUser(uuser_id, uprops):
    try:
        result = BSFindUser(uuser_id, uprops)
        return result

    except Exception as e:
        logging.error(e)