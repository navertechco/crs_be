try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSLogPay import FSLogPay
from .BSLogPay import BSLogPay
from .DSLogPay import DSLogPay


class LogPay():
    def __init__(self):
        self.FSLogPay = FSLogPay
        self.BSLogPay = BSLogPay
        self.DSLogPay = DSLogPay