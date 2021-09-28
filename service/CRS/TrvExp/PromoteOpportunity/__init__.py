try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSPromoteOpportunity import FSPromoteOpportunity
from .BSPromoteOpportunity import BSPromoteOpportunity
from .DSPromoteOpportunity import DSPromoteOpportunity


class PromoteOpportunity():
    def __init__(self):
        self.FSPromoteOpportunity = FSPromoteOpportunity
        self.BSPromoteOpportunity = BSPromoteOpportunity
        self.DSPromoteOpportunity = DSPromoteOpportunity