try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSCreateActivity import FSCreateActivity
from .BSCreateActivity import BSCreateActivity
from .DSCreateActivity import DSCreateActivity


class CreateActivity():
    def __init__(self):
        self.FSCreateActivity = FSCreateActivity
        self.BSCreateActivity = BSCreateActivity
        self.DSCreateActivity = DSCreateActivity