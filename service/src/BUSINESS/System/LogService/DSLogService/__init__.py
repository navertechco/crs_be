try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
# from ..Core import Business
from naver_core import *

def DSLogService(udata):
    try:
        business = Business(mySession)
        result = business.method(udata)
        return result

    except Exception as e:
        raise e