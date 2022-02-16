try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSValidateService import BSValidateService
from naver_core import *

def FSValidateService(udata):
    try:
        result = BSValidateService(udata)
        return Ok(result)

    except Exception as e:
        ErrorResponse(e)