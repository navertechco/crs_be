try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSGetExperienceList import FSGetExperienceList
from .BSGetExperienceList import BSGetExperienceList
from .DSGetExperienceList import DSGetExperienceList


class GetExperienceList():
    def __init__(self):
        self.FSGetExperienceList = FSGetExperienceList
        self.BSGetExperienceList = BSGetExperienceList
        self.DSGetExperienceList = DSGetExperienceList