try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSEditActivity import FSEditActivity
from .BSEditActivity import BSEditActivity
from .DSEditActivity import DSEditActivity


class EditActivity():
    def __init__(self):
        self.FSEditActivity = FSEditActivity
        self.BSEditActivity = BSEditActivity
        self.DSEditActivity = DSEditActivity