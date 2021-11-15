from .EditOpportunity import EditOpportunity
from .CreateOpportunity import CreateOpportunity
from .ListOpportunityDetail import ListOpportunityDetail
from .ListAllOpportunity import ListAllOpportunity
from .EditContact import EditContact
from .CreateContact import CreateContact
from .ListContactDetail import ListContactDetail
from .ListAllContact import ListAllContact
from .JoinPoll import JoinPoll
from ..User import User
try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
class Agent(User):
    def __init__(self):
        self.JoinPoll = JoinPoll()
        self.ListAllContact = ListAllContact()
        self.ListContactDetail = ListContactDetail()
        self.CreateContact = CreateContact()
        self.EditContact = EditContact()
        self.ListAllOpportunity = ListAllOpportunity()
        self.ListOpportunityDetail = ListOpportunityDetail()
        self.CreateOpportunity = CreateOpportunity()
        self.EditOpportunity = EditOpportunity()
        self.attributes={self.props: None , self.agent_id: None , self.agent_type: None }
