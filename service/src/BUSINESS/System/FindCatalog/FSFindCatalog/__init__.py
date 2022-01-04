try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSFindCatalog import BSFindCatalog
from naver_core import *

def FSFindCatalog(input):
    try: 
        result = BSFindCatalog(input)
        return result

    except Exception as e:
        return ErrorResponse(e) 