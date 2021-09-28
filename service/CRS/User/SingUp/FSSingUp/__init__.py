try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSSingUp import BSSingUp
import logging

def FSSingUp(uusername, upassword):
    try:
        result = BSSingUp(uusername, upassword)
        return result

    except Exception as e:
        logging.error(e)