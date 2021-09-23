try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
# from ..Core import Business
import logging

def DSGetPollDetail(upoll_id):
    try:
        business = Business(mySession)
        result = business.method(upoll_id)
        return result

    except Exception as e:
        logging.error(e)