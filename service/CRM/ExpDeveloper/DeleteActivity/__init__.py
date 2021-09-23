try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSDeleteActivity import FSDeleteActivity
from .BSDeleteActivity import BSDeleteActivity
from .DSDeleteActivity import DSDeleteActivity


class DeleteActivity():
    def __init__(self):
        self.FSDeleteActivity = FSDeleteActivity
        self.BSDeleteActivity = BSDeleteActivity
        self.DSDeleteActivity = DSDeleteActivity