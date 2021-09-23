try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSDeleteUser import BSDeleteUser
import logging

def FSDeleteUser(uuser_id):
    try:
        result = BSDeleteUser(uuser_id)
        return result

    except Exception as e:
        logging.error(e)