try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSDeleteExperience import FSDeleteExperience
from .BSDeleteExperience import BSDeleteExperience
from .DSDeleteExperience import DSDeleteExperience


class DeleteExperience():
    def __init__(self):
        self.FSDeleteExperience = FSDeleteExperience
        self.BSDeleteExperience = BSDeleteExperience
        self.DSDeleteExperience = DSDeleteExperience