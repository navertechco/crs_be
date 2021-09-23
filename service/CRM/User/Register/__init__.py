try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSRegister import FSRegister
from .BSRegister import BSRegister
from .DSRegister import DSRegister


class Register():
    def __init__(self):
        self.FSRegister = FSRegister
        self.BSRegister = BSRegister
        self.DSRegister = DSRegister