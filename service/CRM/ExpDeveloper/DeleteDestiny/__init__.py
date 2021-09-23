try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSDeleteDestiny import FSDeleteDestiny
from .BSDeleteDestiny import BSDeleteDestiny
from .DSDeleteDestiny import DSDeleteDestiny


class DeleteDestiny():
    def __init__(self):
        self.FSDeleteDestiny = FSDeleteDestiny
        self.BSDeleteDestiny = BSDeleteDestiny
        self.DSDeleteDestiny = DSDeleteDestiny