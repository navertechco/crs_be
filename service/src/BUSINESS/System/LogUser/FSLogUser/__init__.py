try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSLogUser import BSLogUser
from naver_core import *

def FSLogUser(udata):
    try:
        result = BSLogUser(udata)
        return Ok(result)

    except Exception as e:
        ErrorResponse(e)