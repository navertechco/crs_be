try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSListPermission import BSListPermission
import logging

def FSListPermission(uemail):
    try:
        result = BSListPermission(uemail)
        return result

    except Exception as e:
        logging.error(e)