from .EditProduct import EditProduct
from .CreateProduct import CreateProduct
from .ListProductDetail import ListProductDetail
from .ListAllProduct import ListAllProduct
from .EditService import EditService
from .CreateService import CreateService
from .ListServiceDetail import ListServiceDetail
from .ListAllService import ListAllService
from .EditActivity import EditActivity
from .CreateActivity import CreateActivity
from .ListActivityDetail import ListActivityDetail
from .ListAllActivity import ListAllActivity
from .EditDestiny import EditDestiny
from .CreateDestiny import CreateDestiny
from .ListDestinyDetail import ListDestinyDetail
from .ListAllDestiny import ListAllDestiny
from .EditExperience import EditExperience
from .CreateExperience import CreateExperience
from .ListExperienceDetail import ListExperienceDetail
from .ListAllExperience import ListAllExperience
from .EditSupplier import EditSupplier
from .CreateSupplier import CreateSupplier
from .ListSupplierDetail import ListSupplierDetail
from .ListAllSupplier import ListAllSupplier
from .EditPoll import EditPoll
from .CreatePoll import CreatePoll
from .ListPollDetail import ListPollDetail
from .ListAllPoll import ListAllPoll
from .EditTour import EditTour
from .CreateTour import CreateTour
from .ListTourDetail import ListTourDetail
from .ListAllTour import ListAllTour
from .EditCatalogue import EditCatalogue
from .CreateCatalogue import CreateCatalogue
from .ListCatalogueDetail import ListCatalogueDetail
from .ListAllCatalogue import ListAllCatalogue
from .EditMedia import EditMedia
from .CreateMedia import CreateMedia
from .ListMediaDetail import ListMediaDetail
from .ListAllMedia import ListAllMedia
from ..User import User
try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
class ExpDeveloper(User):
    def __init__(self):
        self.ListAllMedia = ListAllMedia()
        self.ListMediaDetail = ListMediaDetail()
        self.CreateMedia = CreateMedia()
        self.EditMedia = EditMedia()
        self.ListAllCatalogue = ListAllCatalogue()
        self.ListCatalogueDetail = ListCatalogueDetail()
        self.CreateCatalogue = CreateCatalogue()
        self.EditCatalogue = EditCatalogue()
        self.ListAllTour = ListAllTour()
        self.ListTourDetail = ListTourDetail()
        self.CreateTour = CreateTour()
        self.EditTour = EditTour()
        self.ListAllPoll = ListAllPoll()
        self.ListPollDetail = ListPollDetail()
        self.CreatePoll = CreatePoll()
        self.EditPoll = EditPoll()
        self.ListAllSupplier = ListAllSupplier()
        self.ListSupplierDetail = ListSupplierDetail()
        self.CreateSupplier = CreateSupplier()
        self.EditSupplier = EditSupplier()
        self.ListAllExperience = ListAllExperience()
        self.ListExperienceDetail = ListExperienceDetail()
        self.CreateExperience = CreateExperience()
        self.EditExperience = EditExperience()
        self.ListAllDestiny = ListAllDestiny()
        self.ListDestinyDetail = ListDestinyDetail()
        self.CreateDestiny = CreateDestiny()
        self.EditDestiny = EditDestiny()
        self.ListAllActivity = ListAllActivity()
        self.ListActivityDetail = ListActivityDetail()
        self.CreateActivity = CreateActivity()
        self.EditActivity = EditActivity()
        self.ListAllService = ListAllService()
        self.ListServiceDetail = ListServiceDetail()
        self.CreateService = CreateService()
        self.EditService = EditService()
        self.ListAllProduct = ListAllProduct()
        self.ListProductDetail = ListProductDetail()
        self.CreateProduct = CreateProduct()
        self.EditProduct = EditProduct()
        self.attributes={self.expDev_id: None , self.props: None , self.expDev_type: None }
