try:
    __import__("pkg_resources").declare_namespace(__name__)
except ImportError:
    __path__ = __import__("pkgutil").extend_path(__path__, __name__)
from src.business.Dto import DayDto, ExperienceDto, DayDetailDto, ServiceDto
from naver_db import NaverDB
from naver_config import NaverConfig
from naver_core import *
from src.infra.web.app.routes import app
from src.business.System.GetNextVal import DSGetNextVal

config = NaverConfig(app)
nbd = NaverDB(app, config)


def DSProcessDays(tour_id, destination):
    """Método de Persistencia para procresar dias de un Tour
    Args:
        tour_id (int): identificacion del tour
        destination (dict): destino
    Raises:
        e: error de proceso
    Returns:
        res: resultado de la operación
    """
    try:
        # return True
        schema = "entities"
        table = "TOUR_DETAIL"
        stm = " SELECT * "
        stm += f"   FROM {schema}.{table} TDTL"
        stm += f"   WHERE TDTL.TOUR_ID = '{tour_id}'"
        tour_detail = nbd.persistence.getQuery(stm, table)
        if len(tour_detail) > 0:
            for destination in tour_detail:
                destData = prepareJsonData(destination.get("detail"))
                tour_detail_id = destData.get("tour_detail_id")
                days = prepareJsonData(destData.get("daysData"))
                index = 0
                for day in days:
                    last_row_id = DSGetNextVal("DAY", "day_id")
                    day_dto = DayDto(day)
                    day_dto.set("tour_detail_id",
                                tour_detail_id)
                    day_dto.set("day_id", last_row_id)
                    index += 1
                    table = "DAY"
                    res = nbd.persistence.insertDto(day_dto, table)
                    if len(res) > 0:
                        res["session"].commit()
                    else:
                        raise Exception(605, "Error de Procesamiento de días")
            return True
        raise Exception(605, "Error de Procesamiento de servicios")
    except Exception as e:
        raise e
