try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSValidateActivity import DSValidateActivity
import logging

def BSValidateActivity(udata):
    try:
        result = DSValidateActivity(udata)
        return result

    except Exception as e:
        logging.error(e)