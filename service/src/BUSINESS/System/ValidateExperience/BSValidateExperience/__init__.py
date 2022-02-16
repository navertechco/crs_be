try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSValidateExperience import DSValidateExperience
from naver_core import *

def BSValidateExperience(udata):
    try:
        result = DSValidateExperience(udata)
        return result

    except Exception as e:
        raise e