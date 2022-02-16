try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSValidatePay import DSValidatePay
import logging

def BSValidatePay(udata):
    try:
        result = DSValidatePay(udata)
        return result

    except Exception as e:
        raise e