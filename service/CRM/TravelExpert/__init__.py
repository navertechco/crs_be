from .CancelTour import CancelTour
from .GetQuoteList import GetQuoteList
from .FindQuote import FindQuote
from .UpdateQuote import UpdateQuote
from .GetQuoteDetail import GetQuoteDetail
from .DeleteQuote import DeleteQuote
from .CreateQuote import CreateQuote
from .GetUpSellingList import GetUpSellingList
from .FindUpSelling import FindUpSelling
from .UpdateUpSelling import UpdateUpSelling
from .GetUpSellingDetail import GetUpSellingDetail
from .DeleteUpSelling import DeleteUpSelling
from .CreateUpSelling import CreateUpSelling
from ..User import User
try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
class TravelExpert(User):
    def __init__(self):
        self.CreateUpSelling = CreateUpSelling()
        self.DeleteUpSelling = DeleteUpSelling()
        self.GetUpSellingDetail = GetUpSellingDetail()
        self.UpdateUpSelling = UpdateUpSelling()
        self.FindUpSelling = FindUpSelling()
        self.GetUpSellingList = GetUpSellingList()
        self.CreateQuote = CreateQuote()
        self.DeleteQuote = DeleteQuote()
        self.GetQuoteDetail = GetQuoteDetail()
        self.UpdateQuote = UpdateQuote()
        self.FindQuote = FindQuote()
        self.GetQuoteList = GetQuoteList()
        self.CancelTour = CancelTour()
        self.attributes={self.travexp_type: None , self.travexp_id: None , self.props: None }
