try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSEdit import FSEdit
from .BSEdit import BSEdit
from .DSEdit import DSEdit


class Edit():
    def __init__(self):
        self.FSEdit = FSEdit
        self.BSEdit = BSEdit
        self.DSEdit = DSEdit