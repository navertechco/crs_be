try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSResetPassword import FSResetPassword
from .BSResetPassword import BSResetPassword
from .DSResetPassword import DSResetPassword


class ResetPassword():
    def __init__(self):
        self.FSResetPassword = FSResetPassword
        self.BSResetPassword = BSResetPassword
        self.DSResetPassword = DSResetPassword