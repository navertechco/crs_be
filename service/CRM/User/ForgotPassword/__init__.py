try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSForgotPassword import FSForgotPassword
from .BSForgotPassword import BSForgotPassword
from .DSForgotPassword import DSForgotPassword


class ForgotPassword():
    def __init__(self):
        self.FSForgotPassword = FSForgotPassword
        self.BSForgotPassword = BSForgotPassword
        self.DSForgotPassword = DSForgotPassword