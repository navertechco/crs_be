from .GetVideoList import GetVideoList
from .FindVideo import FindVideo
from .UpdateVideo import UpdateVideo
from .DeleteVideo import DeleteVideo
from .CreateVideo import CreateVideo
from .GetExperienceList import GetExperienceList
from .FindExperience import FindExperience
from .UpdateExperience import UpdateExperience
from .GetExperienceDetail import GetExperienceDetail
from .DeleteExperience import DeleteExperience
from .CreateExperience import CreateExperience
from .GetActivityList import GetActivityList
from .FindActivity import FindActivity
from .UpdateActivity import UpdateActivity
from .GetActivityDetail import GetActivityDetail
from .DeleteActivity import DeleteActivity
from .CreateActivity import CreateActivity
from .GetDestinyList import GetDestinyList
from .FindDestiny import FindDestiny
from .UpdateDestiny import UpdateDestiny
from .GetDestinyDetail import GetDestinyDetail
from .DeleteDestiny import DeleteDestiny
from .CreateDestiny import CreateDestiny
from .GetSupplierList import GetSupplierList
from .FindSupplier import FindSupplier
from .UpdateSupplier import UpdateSupplier
from .DeleteSupplier import DeleteSupplier
from .CreateSupplier import CreateSupplier
from ..User import User
try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
class ExpDeveloper(User):
    def __init__(self):
        self.CreateSupplier = CreateSupplier()
        self.DeleteSupplier = DeleteSupplier()
        self.UpdateSupplier = UpdateSupplier()
        self.FindSupplier = FindSupplier()
        self.GetSupplierList = GetSupplierList()
        self.CreateDestiny = CreateDestiny()
        self.DeleteDestiny = DeleteDestiny()
        self.GetDestinyDetail = GetDestinyDetail()
        self.UpdateDestiny = UpdateDestiny()
        self.FindDestiny = FindDestiny()
        self.GetDestinyList = GetDestinyList()
        self.CreateActivity = CreateActivity()
        self.DeleteActivity = DeleteActivity()
        self.GetActivityDetail = GetActivityDetail()
        self.UpdateActivity = UpdateActivity()
        self.FindActivity = FindActivity()
        self.GetActivityList = GetActivityList()
        self.CreateExperience = CreateExperience()
        self.DeleteExperience = DeleteExperience()
        self.GetExperienceDetail = GetExperienceDetail()
        self.UpdateExperience = UpdateExperience()
        self.FindExperience = FindExperience()
        self.GetExperienceList = GetExperienceList()
        self.CreateVideo = CreateVideo()
        self.DeleteVideo = DeleteVideo()
        self.UpdateVideo = UpdateVideo()
        self.FindVideo = FindVideo()
        self.GetVideoList = GetVideoList()
        self.attributes={self.expdev_id: None , self.props: None , self.expdev_type: None }
