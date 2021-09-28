try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSListProblemDetail import FSListProblemDetail
from .BSListProblemDetail import BSListProblemDetail
from .DSListProblemDetail import DSListProblemDetail


class ListProblemDetail():
    def __init__(self):
        self.FSListProblemDetail = FSListProblemDetail
        self.BSListProblemDetail = BSListProblemDetail
        self.DSListProblemDetail = DSListProblemDetail