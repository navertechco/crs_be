try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSForgot import DSForgot
import logging

def BSForgot(uemail):
    try:
        result = DSForgot(uemail)
        return result

    except Exception as e:
        logging.error(e)