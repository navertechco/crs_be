try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSGetUserList import DSGetUserList
import logging

def BSGetUserList():
    try:
        result = DSGetUserList()
        return result

    except Exception as e:
        logging.error(e)