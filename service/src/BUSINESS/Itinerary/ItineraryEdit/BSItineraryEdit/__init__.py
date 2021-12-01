try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSItineraryEdit import DSItineraryEdit
from naver_core import *
from ... import NewItinerary, ProcessItinerary, UpdateItinerary


def BSItineraryEdit(input):
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
            valid = DSItineraryEdit(input)
            if valid:
                intinerary_id = NewItinerary().BSNewItinerary(input)
                if intinerary_id is not None:
                    done = ProcessItinerary().BSProcessItinerary(intinerary_id, input)
                    if done:
                        return done
                    raise Exception('Error al procesar la cotización')
                raise Exception('Error al crear la cotización')
            raise Exception('Ya tiene una cotización activa')

        if state == 'update':
            return UpdateItinerary().BSUpdateItinerary(input)

        raise Exception(605, 'Error de Edición')
    except Exception as e:
        raise e
