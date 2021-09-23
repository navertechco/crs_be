try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSRegister import DSRegister
import logging

def BSRegister(uusername, upassword):
    try:
        result = DSRegister(uusername, upassword)
        return result

    except Exception as e:
        logging.error(e)