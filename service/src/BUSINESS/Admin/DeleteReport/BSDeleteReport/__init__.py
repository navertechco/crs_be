try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSDeleteReport import DSDeleteReport
import logging

def BSDeleteReport(udata):
    try:
        result = DSDeleteReport(udata)
        return result

    except Exception as e:
        raise e