try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSNewMatch import DSNewMatch 
from naver_core import *


def BSNewMatch(id, match):
    """Método para procesar match de cotización

    Args:
        id (int): Identificador de la Cotización
        match (list): Lista de Match

    Raises:
        Exception: Error de conexión con el servicio de Naver
        e: Error de procesamiento de la Cotización

    Returns:
        bool: True si la Cotización fue procesada correctamente, False en caso contrario
    """
    try: 
        res =  DSNewMatch(id, match)
        if len(res) > 0:
            res['session'].commit()
            return True
        raise Exception((605, 'Error de NewMatchación'))
    except Exception as e:
        raise e
