try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSSingUp import DSSingUp
import logging

def BSSingUp(uusername, upassword):
    try:
        result = DSSingUp(uusername, upassword)
        return result

    except Exception as e:
        logging.error(e)