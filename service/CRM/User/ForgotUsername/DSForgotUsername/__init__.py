try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
# from ..Core import Business
import logging

def DSForgotUsername(uemail):
    try:
        business = Business(mySession)
        result = business.method(uemail)
        return result

    except Exception as e:
        logging.error(e)