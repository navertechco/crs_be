try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSGetNextVal import DSGetNextVal
import logging

def BSGetNextVal(table, field):
    try:
        result = DSGetNextVal(table, field)
        return result

    except Exception as e:
        logging.error(e)