try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSUpdateExperience import FSUpdateExperience
from .BSUpdateExperience import BSUpdateExperience
from .DSUpdateExperience import DSUpdateExperience


class UpdateExperience():
    def __init__(self):
        self.FSUpdateExperience = FSUpdateExperience
        self.BSUpdateExperience = BSUpdateExperience
        self.DSUpdateExperience = DSUpdateExperience