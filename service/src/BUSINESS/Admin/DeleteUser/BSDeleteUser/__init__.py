try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSDeleteUser import DSDeleteUser
from naver_core import *

def BSDeleteUser(udata):
    try:
        result = DSDeleteUser(udata)
        return result

    except Exception as e:
        raise e