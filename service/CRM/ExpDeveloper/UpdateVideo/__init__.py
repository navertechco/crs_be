try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSUpdateVideo import FSUpdateVideo
from .BSUpdateVideo import BSUpdateVideo
from .DSUpdateVideo import DSUpdateVideo


class UpdateVideo():
    def __init__(self):
        self.FSUpdateVideo = FSUpdateVideo
        self.BSUpdateVideo = BSUpdateVideo
        self.DSUpdateVideo = DSUpdateVideo