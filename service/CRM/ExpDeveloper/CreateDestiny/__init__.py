try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSCreateDestiny import FSCreateDestiny
from .BSCreateDestiny import BSCreateDestiny
from .DSCreateDestiny import DSCreateDestiny


class CreateDestiny():
    def __init__(self):
        self.FSCreateDestiny = FSCreateDestiny
        self.BSCreateDestiny = BSCreateDestiny
        self.DSCreateDestiny = DSCreateDestiny