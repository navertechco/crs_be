try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSListAllPoll import DSListAllPoll
import logging

def BSListAllPoll(udata):
    try:
        result = DSListAllPoll(udata)
        return result

    except Exception as e:
        logging.error(e)