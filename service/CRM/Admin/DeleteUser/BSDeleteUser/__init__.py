try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSDeleteUser import DSDeleteUser
import logging

def BSDeleteUser(uuser_id):
    try:
        result = DSDeleteUser(uuser_id)
        return result

    except Exception as e:
        logging.error(e)