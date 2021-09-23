try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSCreateVideo import FSCreateVideo
from .BSCreateVideo import BSCreateVideo
from .DSCreateVideo import DSCreateVideo


class CreateVideo():
    def __init__(self):
        self.FSCreateVideo = FSCreateVideo
        self.BSCreateVideo = BSCreateVideo
        self.DSCreateVideo = DSCreateVideo