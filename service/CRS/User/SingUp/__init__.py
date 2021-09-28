try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSSingUp import FSSingUp
from .BSSingUp import BSSingUp
from .DSSingUp import DSSingUp


class SingUp():
    def __init__(self):
        self.FSSingUp = FSSingUp
        self.BSSingUp = BSSingUp
        self.DSSingUp = DSSingUp