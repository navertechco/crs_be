try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSGetTheme import FSGetTheme
from .BSGetTheme import BSGetTheme
from .DSGetTheme import DSGetTheme


class GetTheme():
    def __init__(self):
        self.FSGetTheme = FSGetTheme
        self.BSGetTheme = BSGetTheme
        self.DSGetTheme = DSGetTheme