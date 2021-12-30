try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSTourEdit import DSTourEdit
from naver_core import *
from ... import NewTour, ProcessTour, UpdateTour


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
        state = getValue(input, 'state')

        if state == 'new':
            valid = DSTourEdit(input)
            if valid:
                itinerary_id = NewTour().BSNewTour(input)
                if itinerary_id is not None:
                    done = ProcessTour().BSProcessTour(itinerary_id, input)
                    if done:
                        return done
                    raise Exception('Error al procesar la cotización')
                raise Exception('Error al crear la cotización')
            raise Exception('Ya tiene una cotización activa')

        if state == 'update':
            return UpdateTour().BSUpdateTour(input)

        raise Exception(605, 'Error de Edición')
    except Exception as e:
        raise e
