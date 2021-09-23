try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSGetUserDetail import DSGetUserDetail
import logging

def BSGetUserDetail(uuser_id):
    try:
        result = DSGetUserDetail(uuser_id)
        return result

    except Exception as e:
        logging.error(e)