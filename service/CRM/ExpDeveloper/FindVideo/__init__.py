try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSFindVideo import FSFindVideo
from .BSFindVideo import BSFindVideo
from .DSFindVideo import DSFindVideo


class FindVideo():
    def __init__(self):
        self.FSFindVideo = FSFindVideo
        self.BSFindVideo = BSFindVideo
        self.DSFindVideo = DSFindVideo