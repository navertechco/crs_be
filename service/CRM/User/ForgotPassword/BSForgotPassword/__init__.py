try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSForgotPassword import DSForgotPassword
import logging

def BSForgotPassword(uemail):
    try:
        result = DSForgotPassword(uemail)
        return result

    except Exception as e:
        logging.error(e)