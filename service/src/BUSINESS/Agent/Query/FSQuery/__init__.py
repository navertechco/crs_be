try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSQuery import BSQuery
from naver_core import *

def FSQuery(udata):
    try:
        result = BSQuery(udata)
        return Ok((result))

    except Exception as e:
        return ErrorResponse(e)