try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSListReportDetail import DSListReportDetail
from naver_core import *

def BSListReportDetail(udata):
    try:
        result = DSListReportDetail(udata)
        return result

    except Exception as e:
        raise e