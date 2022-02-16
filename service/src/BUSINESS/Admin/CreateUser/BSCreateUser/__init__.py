try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSCreateUser import DSCreateUser
import logging

def BSCreateUser(udata):
    try:
        result = DSCreateUser(udata)
        return result

    except Exception as e:
        raise e