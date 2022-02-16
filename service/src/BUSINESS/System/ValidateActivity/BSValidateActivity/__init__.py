try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSValidateActivity import DSValidateActivity
from naver_core import *

def BSValidateActivity(udata):
    try:
        result = DSValidateActivity(udata)
        return result

    except Exception as e:
        raise e