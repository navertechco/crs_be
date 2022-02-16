try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSValidateOpportunity import DSValidateOpportunity
from naver_core import *

def BSValidateOpportunity(udata):
    try:
        result = DSValidateOpportunity(udata)
        return result

    except Exception as e:
        raise e