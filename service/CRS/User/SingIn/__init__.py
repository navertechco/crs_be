try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSSingIn import FSSingIn
from .BSSingIn import BSSingIn
from .DSSingIn import DSSingIn


class SingIn():
    def __init__(self):
        self.FSSingIn = FSSingIn
        self.BSSingIn = BSSingIn
        self.DSSingIn = DSSingIn