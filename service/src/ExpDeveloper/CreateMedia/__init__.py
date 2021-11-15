try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSCreateMedia import FSCreateMedia
from .BSCreateMedia import BSCreateMedia
from .DSCreateMedia import DSCreateMedia


class CreateMedia():
    def __init__(self):
        self.FSCreateMedia = FSCreateMedia
        self.BSCreateMedia = BSCreateMedia
        self.DSCreateMedia = DSCreateMedia