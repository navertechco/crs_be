try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSSingIn import BSSingIn
import logging

def FSSingIn(uusername, upassword):
    try:
        result = BSSingIn(uusername, upassword)
        return result

    except Exception as e:
        logging.error(e)