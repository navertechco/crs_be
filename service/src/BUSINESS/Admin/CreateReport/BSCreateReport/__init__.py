try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSCreateReport import DSCreateReport
from naver_core import *

def BSCreateReport(udata):
    try:
        result = DSCreateReport(udata)
        return result

    except Exception as e:
        raise e