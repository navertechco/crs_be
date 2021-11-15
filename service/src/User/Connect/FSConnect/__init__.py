try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSConnect import BSConnect
from naver_core import *

def FSConnect(input):
    """Método para crear un nuevo Reporte.
    Args:
        input (dict): Diccionario con los datos del Reporte.

    Returns:
        json: Resultado del API.
    """
    try:
        input["data"]["password"] = "jcuevas123!"
        input["data"]["state"] = "signin"
        result = BSConnect(input)
        if isinstance(result, dict):
            return Ok(result)
        return result

            
        
    except Exception as e:
        return ErrorResponse(e) 