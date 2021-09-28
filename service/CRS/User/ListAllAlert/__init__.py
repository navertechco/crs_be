try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSListAllAlert import FSListAllAlert
from .BSListAllAlert import BSListAllAlert
from .DSListAllAlert import DSListAllAlert


class ListAllAlert():
    def __init__(self):
        self.FSListAllAlert = FSListAllAlert
        self.BSListAllAlert = BSListAllAlert
        self.DSListAllAlert = DSListAllAlert