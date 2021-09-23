try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSGetDestinyList import DSGetDestinyList
import logging

def BSGetDestinyList():
    try:
        result = DSGetDestinyList()
        return result

    except Exception as e:
        logging.error(e)