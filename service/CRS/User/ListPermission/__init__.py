try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSListPermission import FSListPermission
from .BSListPermission import BSListPermission
from .DSListPermission import DSListPermission


class ListPermission():
    def __init__(self):
        self.FSListPermission = FSListPermission
        self.BSListPermission = BSListPermission
        self.DSListPermission = DSListPermission