try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)

from .NewMatch import *
from .NewQuote import *
from .ProcessQuote import *
from .PromoteQuote import *
from .UpdateQuote import *
from .ProcessDestinations import *
from .QuoteEdit import *