try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSAssignTravelExpert import FSAssignTravelExpert
from .BSAssignTravelExpert import BSAssignTravelExpert
from .DSAssignTravelExpert import DSAssignTravelExpert


class AssignTravelExpert():
    def __init__(self):
        self.FSAssignTravelExpert = FSAssignTravelExpert
        self.BSAssignTravelExpert = BSAssignTravelExpert
        self.DSAssignTravelExpert = DSAssignTravelExpert