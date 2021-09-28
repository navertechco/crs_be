try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSListAllActivity import FSListAllActivity
from .BSListAllActivity import BSListAllActivity
from .DSListAllActivity import DSListAllActivity


class ListAllActivity():
    def __init__(self):
        self.FSListAllActivity = FSListAllActivity
        self.BSListAllActivity = BSListAllActivity
        self.DSListAllActivity = DSListAllActivity