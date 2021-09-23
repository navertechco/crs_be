try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSFindExperience import FSFindExperience
from .BSFindExperience import BSFindExperience
from .DSFindExperience import DSFindExperience


class FindExperience():
    def __init__(self):
        self.FSFindExperience = FSFindExperience
        self.BSFindExperience = BSFindExperience
        self.DSFindExperience = DSFindExperience