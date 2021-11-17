try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSListAllProblem import FSListAllProblem
from .BSListAllProblem import BSListAllProblem
from .DSListAllProblem import DSListAllProblem


class ListAllProblem():
    def __init__(self):
        self.FSListAllProblem = FSListAllProblem
        self.BSListAllProblem = BSListAllProblem
        self.DSListAllProblem = DSListAllProblem