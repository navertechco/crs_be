try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSSendAlert import DSSendAlert
from naver_core import *

def BSSendAlert(udata):
    try:
        result = DSSendAlert(udata)
        return result

    except Exception as e:
        raise e