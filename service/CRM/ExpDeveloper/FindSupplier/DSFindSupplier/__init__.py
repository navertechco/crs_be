try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
# from ..Core import Business
import logging

def DSFindSupplier(usupplier_id, ucontact_id, uprops):
    try:
        business = Business(mySession)
        result = business.method(usupplier_id, ucontact_id, uprops)
        return result

    except Exception as e:
        logging.error(e)