try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSForgotUsername import FSForgotUsername
from .BSForgotUsername import BSForgotUsername
from .DSForgotUsername import DSForgotUsername


class ForgotUsername():
    def __init__(self):
        self.FSForgotUsername = FSForgotUsername
        self.BSForgotUsername = BSForgotUsername
        self.DSForgotUsername = DSForgotUsername