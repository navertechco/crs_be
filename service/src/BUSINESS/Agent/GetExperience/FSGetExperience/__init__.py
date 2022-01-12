try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSGetExperience import BSGetExperience
from naver_core import *

def FSGetExperience(input):
    try:
        name = getValue(input, 'name')
        result = BSGetExperience(name)
        return Ok((result))

    except Exception as e:
        ErrorResponse(e)