try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSValidateQuote import FSValidateQuote
from .BSValidateQuote import BSValidateQuote
from .DSValidateQuote import DSValidateQuote


class ValidateQuote():
    def __init__(self):
        self.FSValidateQuote = FSValidateQuote
        self.BSValidateQuote = BSValidateQuote
        self.DSValidateQuote = DSValidateQuote