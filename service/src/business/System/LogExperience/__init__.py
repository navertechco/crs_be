try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSLogExperience import FSLogExperience
from .BSLogExperience import BSLogExperience
from .DSLogExperience import DSLogExperience


class LogExperience():
    def __init__(self):
        self.FSLogExperience = FSLogExperience
        self.BSLogExperience = BSLogExperience
        self.DSLogExperience = DSLogExperience