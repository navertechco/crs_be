try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSLoadTemplate import DSLoadTemplate
import logging

def BSLoadTemplate(udata):
    try:
        result = DSLoadTemplate(udata)
        return result

    except Exception as e:
        logging.error(e)