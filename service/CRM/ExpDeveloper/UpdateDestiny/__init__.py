try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSUpdateDestiny import FSUpdateDestiny
from .BSUpdateDestiny import BSUpdateDestiny
from .DSUpdateDestiny import DSUpdateDestiny


class UpdateDestiny():
    def __init__(self):
        self.FSUpdateDestiny = FSUpdateDestiny
        self.BSUpdateDestiny = BSUpdateDestiny
        self.DSUpdateDestiny = DSUpdateDestiny