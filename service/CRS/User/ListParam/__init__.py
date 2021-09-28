try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSListParam import FSListParam
from .BSListParam import BSListParam
from .DSListParam import DSListParam


class ListParam():
    def __init__(self):
        self.FSListParam = FSListParam
        self.BSListParam = BSListParam
        self.DSListParam = DSListParam