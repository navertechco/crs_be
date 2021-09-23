from .GetPollList import GetPollList
from .FindPoll import FindPoll
from .UpdatePoll import UpdatePoll
from .GetPollDetail import GetPollDetail
from .DeletePoll import DeletePoll
from .CreatePoll import CreatePoll
from .GetTourList import GetTourList
from .FindTour import FindTour
from .UpdateTour import UpdateTour
from .GetTourDetail import GetTourDetail
from .DeleteTour import DeleteTour
from .CreateTour import CreateTour
from ..User import User
try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
class Agent(User):
    def __init__(self):
        self.CreateTour = CreateTour()
        self.DeleteTour = DeleteTour()
        self.GetTourDetail = GetTourDetail()
        self.UpdateTour = UpdateTour()
        self.FindTour = FindTour()
        self.GetTourList = GetTourList()
        self.CreatePoll = CreatePoll()
        self.DeletePoll = DeletePoll()
        self.GetPollDetail = GetPollDetail()
        self.UpdatePoll = UpdatePoll()
        self.FindPoll = FindPoll()
        self.GetPollList = GetPollList()
        self.attributes={self.props: None , self.agent_id: None , self.agent_type: None }
