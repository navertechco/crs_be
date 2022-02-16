try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSLogProblem import DSLogProblem
from naver_core import *

def BSLogProblem(udata):
    try:
        result = DSLogProblem(udata)
        return result

    except Exception as e:
        raise e