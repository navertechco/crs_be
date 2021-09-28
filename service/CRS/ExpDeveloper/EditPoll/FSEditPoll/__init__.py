try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSEditPoll import BSEditPoll
import logging

def FSEditPoll(udata):
    try:
        result = BSEditPoll(udata)
        return result

    except Exception as e:
        logging.error(e)