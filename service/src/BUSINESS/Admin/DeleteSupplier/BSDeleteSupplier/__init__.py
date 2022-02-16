try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSDeleteSupplier import DSDeleteSupplier
from naver_core import *

def BSDeleteSupplier(udata):
    try:
        result = DSDeleteSupplier(udata)
        return result

    except Exception as e:
        raise e