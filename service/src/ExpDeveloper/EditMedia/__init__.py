try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSEditMedia import FSEditMedia
from .BSEditMedia import BSEditMedia
from .DSEditMedia import DSEditMedia


class EditMedia():
    def __init__(self):
        self.FSEditMedia = FSEditMedia
        self.BSEditMedia = BSEditMedia
        self.DSEditMedia = DSEditMedia