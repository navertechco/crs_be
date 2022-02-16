try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSValidateService import DSValidateService
from naver_core import *

def BSValidateService(udata):
    try:
        result = DSValidateService(udata)
        return result

    except Exception as e:
        raise e