try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSGetTourDetail import BSGetTourDetail
import logging

def FSGetTourDetail(utour_id):
    try:
        result = BSGetTourDetail(utour_id)
        return result

    except Exception as e:
        logging.error(e)