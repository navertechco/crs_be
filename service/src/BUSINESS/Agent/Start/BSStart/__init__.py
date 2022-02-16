try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSStart import DSStart
import logging

def BSStart(udata):
    try:
        result = DSStart(udata)
        return result

    except Exception as e:
        raise e