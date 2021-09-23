from .GetUserList import GetUserList
from .FindUser import FindUser
from .UpdateUser import UpdateUser
from .GetUserDetail import GetUserDetail
from .DeleteUser import DeleteUser
from .CreateUser import CreateUser
from ..User import User
try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
class Admin(User):
    def __init__(self):
        self.CreateUser = CreateUser()
        self.DeleteUser = DeleteUser()
        self.GetUserDetail = GetUserDetail()
        self.UpdateUser = UpdateUser()
        self.FindUser = FindUser()
        self.GetUserList = GetUserList()
        self.attributes={self.admin_type: None , self.props: None , self.admin_id: None }
