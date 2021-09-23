try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSGetUpSellingDetail import BSGetUpSellingDetail
import logging

def FSGetUpSellingDetail(uupselling_id):
    try:
        result = BSGetUpSellingDetail(uupselling_id)
        return result

    except Exception as e:
        logging.error(e)