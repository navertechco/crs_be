try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSListUserDetail import DSListUserDetail
from naver_core import *

def BSListUserDetail(udata):
    try:
        result = DSListUserDetail(udata)
        return result

    except Exception as e:
        raise e