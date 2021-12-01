try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)

from .user import UserDto
from .profile import ProfileDto
from .client import ClientDto
from .intinerary import ItineraryDto
from .destination import DestinationDto, DestinationListDto
from .service import ServiceDto, ServiceListDto