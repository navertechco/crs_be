try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSSendNotification import DSSendNotification
import logging

def BSSendNotification(udata):
    try:
        result = DSSendNotification(udata)
        return result

    except Exception as e:
        raise e