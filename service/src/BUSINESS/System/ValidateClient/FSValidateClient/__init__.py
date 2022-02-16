try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSValidateClient import BSValidateClient
from naver_core import *

def FSValidateClient(input):
    try:
        result = BSValidateClient(input)
        return Ok(result)

    except Exception as e:
        ErrorResponse(e)