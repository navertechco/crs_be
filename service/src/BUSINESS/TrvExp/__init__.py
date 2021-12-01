from .EditTour import EditTour
from .CreateTour import CreateTour
from .ListTourDetail import ListTourDetail
from .ListAllTour import ListAllTour
from .EditProblem import EditProblem
from .CreateProblem import CreateProblem
from .ListProblemDetail import ListProblemDetail
from .ListAllProblem import ListAllProblem
from .EditSale import EditSale
from .CreateSale import CreateSale
from .ListSaleDetail import ListSaleDetail
from .ListAllSale import ListAllSale
from .EditSale import EditSale
from .CreateSale import CreateSale
from .ListSaleDetail import ListSaleDetail
from .ListAllSale import ListAllSale
from .PromoteSale import PromoteSale
from .PromoteOpportunity import PromoteOpportunity
from .PromoteItinerary import PromoteItinerary
from .PromoteContact import PromoteContact
from .EditOpportunity import EditOpportunity
from .CreateOpportunity import CreateOpportunity
from .ListOpportunityDetail import ListOpportunityDetail
from .ListAllOpportunity import ListAllOpportunity

try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
class TrvExp():
    def __init__(self):
        self.ListAllOpportunity = ListAllOpportunity()
        self.ListOpportunityDetail = ListOpportunityDetail()
        self.CreateOpportunity = CreateOpportunity()
        self.EditOpportunity = EditOpportunity()
        self.PromoteContact = PromoteContact()
        self.PromoteItinerary = PromoteItinerary()
        self.PromoteOpportunity = PromoteOpportunity()
        self.PromoteSale = PromoteSale()
        self.ListAllSale = ListAllSale()
        self.ListSaleDetail = ListSaleDetail()
        self.CreateSale = CreateSale()
        self.EditSale = EditSale()
        self.ListAllSale = ListAllSale()
        self.ListSaleDetail = ListSaleDetail()
        self.CreateSale = CreateSale()
        self.EditSale = EditSale()
        self.ListAllProblem = ListAllProblem()
        self.ListProblemDetail = ListProblemDetail()
        self.CreateProblem = CreateProblem()
        self.EditProblem = EditProblem()
        self.ListAllTour = ListAllTour()
        self.ListTourDetail = ListTourDetail()
        self.CreateTour = CreateTour()
        self.EditTour = EditTour()
        self.attributes={self.trvExp_type: None , self.trvExp_id: None , self.props: None }
