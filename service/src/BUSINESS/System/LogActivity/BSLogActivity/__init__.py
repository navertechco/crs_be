try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSLogActivity import DSLogActivity
from naver_core import *

def BSLogActivity(udata):
    try:
        result = DSLogActivity(udata)
        return result

    except Exception as e:
        raise e