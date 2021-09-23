try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSSingIn import DSSingIn
import logging

def BSSingIn(uusername, upassword):
    try:
        result = DSSingIn(uusername, upassword)
        return result

    except Exception as e:
        logging.error(e)