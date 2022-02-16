try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSValidatePoll import DSValidatePoll
import logging

def BSValidatePoll(udata):
    try:
        result = DSValidatePoll(udata)
        return result

    except Exception as e:
        raise e