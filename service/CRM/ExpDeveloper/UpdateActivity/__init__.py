try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSUpdateActivity import FSUpdateActivity
from .BSUpdateActivity import BSUpdateActivity
from .DSUpdateActivity import DSUpdateActivity


class UpdateActivity():
    def __init__(self):
        self.FSUpdateActivity = FSUpdateActivity
        self.BSUpdateActivity = BSUpdateActivity
        self.DSUpdateActivity = DSUpdateActivity