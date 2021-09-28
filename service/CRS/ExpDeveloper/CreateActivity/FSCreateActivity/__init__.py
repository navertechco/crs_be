try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSCreateActivity import BSCreateActivity
import logging

def FSCreateActivity(udata):
    try:
        result = BSCreateActivity(udata)
        return result

    except Exception as e:
        logging.error(e)