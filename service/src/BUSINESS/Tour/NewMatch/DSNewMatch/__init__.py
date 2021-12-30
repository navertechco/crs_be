try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)

from naver_db import NaverDB
from naver_config import NaverConfig
from naver_core import *
from src.INFRA.WEB.App.routes import app


config = NaverConfig(app)
nbd = NaverDB(app, config)


def DSNewMatch(id, match):
    """Método para procesar match de tour 

    Args:
        id (int): Identificador de la Cotización
        match (list): Lista de Match

    Raises:
        e: Exception

    Returns:
        res: Resultado de la Cotización
    """
    try:
        table = "ITINERARY"
        stm = " UPDATE " + table
        stm += " SET match=\'{}\'".format(match)
        stm += ", tour_state_id=3"
        where = " WHERE tour_id = \'{}\'".format(id)
        stm += " " + where
        res = nbd.persistence.setWrite(stm, table)
        return res

    except Exception as e:
        raise e
