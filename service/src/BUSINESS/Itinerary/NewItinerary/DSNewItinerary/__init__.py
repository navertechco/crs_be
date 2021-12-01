try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)

from src.BUSINESS.Dto import ItineraryDto
from src.INFRA.WEB.App.routes import app
from naver_db import NaverDB
from naver_config import NaverConfig
from naver_core import *

config = NaverConfig(app)
nbd = NaverDB(app, config)


def DSNewItinerary(input):
    """Método para crear una cotización en la base de datos.

    Args:
        input (dict): Diccionario con los datos de la cotización.

    Raises:
        e: Error de conexión con la base de datos.

    Returns:
        res: Resultado de la operación.
    """
    try:
        data = input.get('data')
        itinerary = ItineraryDto(data)
        table = "ITINERARY"
        res = nbd.persistence.insertDto(itinerary, table)
        return res

    except Exception as e:
        raise e
