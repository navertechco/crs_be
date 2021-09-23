try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSCreatePoll import BSCreatePoll
import logging

def FSCreatePoll(udata):
    try:
        result = BSCreatePoll(udata)
        return result

    except Exception as e:
        logging.error(e)