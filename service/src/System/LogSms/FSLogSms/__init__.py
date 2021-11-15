try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSLogSms import BSLogSms
import logging

def FSLogSms(udata):
    try:
        result = BSLogSms(udata)
        return result

    except Exception as e:
        logging.error(e)