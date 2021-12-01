try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)

from src.BUSINESS.Dto import ServiceListDto
from naver_db import NaverDB
from naver_config import NaverConfig
from naver_core import *
from src.INFRA.WEB.App.routes import app
import ast
import json

config = NaverConfig(app)
nbd = NaverDB(app, config)


def DSProcessDays(id, input):
    """Método para procesar días de cotización

    Args:
        id (int): Identificador de la Cotización
        input (dict): Diccionario con los datos de la Cotización

    Raises:
        e: Cuando no se puede procesar la Cotización

    Returns:
        res: Resultado de la operación
    """
    try:
        table = "ITINERARY_DAY"
        stm = """
                SELECT QD.ID_ITINERARY_DAY,S.* FROM SERVICE S 
                JOIN ITINERARY_DAY QD 
                ON QD.ID_DESTINATION = S.ID_DESTINATION 
        """
        where = " WHERE QD.ID_ITINERARY = \'{}\'".format(id)
        stm += where
        intinerary_day_services = nbd.persistence.getQuery(stm, table)
        if len(intinerary_day_services) > 0:
            serviceList = ServiceListDto(intinerary_day_services).__list__()
            table = "ITINERARY_DAY_DETAIL"
            stm = nbd.persistence.prepareListDtoToInsert(
                serviceList, table)
            res = nbd.persistence.setWrite(stm, table)
            return res

    except Exception as e:
        raise e
