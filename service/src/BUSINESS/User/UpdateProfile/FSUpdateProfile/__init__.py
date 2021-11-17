try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSUpdateProfile import BSUpdateProfile
from naver_core import *

def FSUpdateProfile	(data):
    """Método para crear un nuevo Reporte.

    Args:
        data (dict): Diccionario con los datos del Reporte.

    Returns:
        json: Resultado del API.
    """
    try:
        result = BSUpdateProfile(data)
        return Ok(result)

    except Exception as e:
        return ErrorResponse(e) 