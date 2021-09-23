try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSDeleteVideo import FSDeleteVideo
from .BSDeleteVideo import BSDeleteVideo
from .DSDeleteVideo import DSDeleteVideo


class DeleteVideo():
    def __init__(self):
        self.FSDeleteVideo = FSDeleteVideo
        self.BSDeleteVideo = BSDeleteVideo
        self.DSDeleteVideo = DSDeleteVideo