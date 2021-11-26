try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSPlayTour import BSPlayTour
from naver_core import *

def FSPlayTour(slug):
    """Método para reproducir una lista de reproduccion de Tour.
    Args:
        slug (str): Slug de la lista de reproduccion de Tour.

    Returns:
        json: Resultado del API.
    """
    try:
 
        result = BSPlayTour(slug)
        return Ok(result)

            
        
    except Exception as e:
        return ErrorResponse(e) 