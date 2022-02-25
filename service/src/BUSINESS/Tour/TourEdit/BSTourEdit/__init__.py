try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSTourEdit import DSTourEdit
from naver_core import *
from ... import NewTour, ProcessTour, UpdateTour, CalculateNetRate


def BSTourEdit(input):
    """Método que se encarga de ejecutar el comando edit.

    Args:
        input (dict): usuario de entrada

    Raises:
        Exception:  Error de validación de usuario

    Returns:
        boolean: True si el usuario se confirma, False si no
    """
    try:
        state = input.get('state')

        if state == 'new':
            valid = DSTourEdit(input)
            if valid:
                tour_id,session = NewTour().BSNewTour(input)
                if tour_id is not None:
                    return ProcessTour().BSProcessTour(tour_id,session, input)
                raise Exception('Error al crear el tour')
            raise Exception('Ya tiene un tour activo')

        if state == 'update':
            return UpdateTour().BSUpdateTour(input)
        if state == 'calculate':
            return CalculateNetRate.BSCalculateNetRate(input)
        raise Exception(605, 'Error de Edición')
    except Exception as e:
        raise e
