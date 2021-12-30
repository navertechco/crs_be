try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSProcessDays import DSProcessDays 
from naver_core import *


def BSProcessDays(id, input):
    """Método para procesar días de tour 	

    Args:
        id (int): Identificador de la Cotización
        input (dict): Diccionario con los datos de la Cotización
    Raises:
        e: Cuando no se puede procesar la Cotización

    Returns:
        res: Resultado de la operación
    """
    try: 
        res =  DSProcessDays(id, input)
        return res
    except Exception as e:
        raise e
