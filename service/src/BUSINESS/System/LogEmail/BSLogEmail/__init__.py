try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSLogEmail import DSLogEmail
from naver_core import *

def BSLogEmail(udata):
    try:
        result = DSLogEmail(udata)
        return result

    except Exception as e:
        raise e