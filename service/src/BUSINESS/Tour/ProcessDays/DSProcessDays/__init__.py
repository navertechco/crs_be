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
        table = "EXPERIENCE"
        select_stm = " SELECT DISTINCT EXPE.experience_id, SRV.service_id"
        from_stm = "    FROM entities.EXPERIENCE EXPE"
        join_stm = """
                            JOIN entities.SERVICE SRV
                                ON EXPE.DESTINATION_ID = SRV.DESTINATION_ID
                            JOIN entities.DESTINATION DEST
                                ON DEST.DESTINATION_ID = EXPE.DESTINATION_ID
                            JOIN entities.TOUR_DETAIL TDTL
                                ON TDTL.DESTINATION_ID = DEST.DESTINATION_ID
        """
        where_stm = "   WHERE TDTL.TOUR_ID = '{}'".format(tour_id)
        stm = select_stm + from_stm + join_stm + where_stm
        services = nbd.persistence.getQuery(stm, table)
        index = 0
        if len(services) > 0:
            days = prepareJsonData(destination.get("days"))
            index = 0
            for day in days:
                last_row_id = DSGetNextVal("DAY", "day_id")
                last_row_id += 1 + index
                day_dto = DayDto(day)
                day_dto.set("tour_detail_id", destination.get("tour_detail_id"))
                day_dto.set("day_id", last_row_id)
                index += 1
                table = "DAY"
                res = nbd.persistence.insertDto(day_dto, table)
                if len(res) > 0:
                    res["session"].commit()
                else:
                    raise Exception(605, "Error de Procesamiento de días")
                experiences = day.get("experiences")
                for experience in experiences:
                    experience_dto = ExperienceDto(experience)
                    print(experience_dto.__dict__())
                    experience_id = experience.get("experience_id")
                    experience_services = [
                        x
                        for x in services
                        if int(x["experience_id"]) == int(experience_id)
                    ]
                    for service in experience_services:
                        day_detail_dto = DayDetailDto({**day_dto.__dict__(), **service})
                        print(day_detail_dto.__dict__())
                        table = "DAY_DETAIL"
                        res = nbd.persistence.insertDto(day_detail_dto, table)
                        if len(res) > 0:
                            res["session"].commit()
                            break
                        else:
                            raise Exception(
                                605, "Error de Procesamiento de experiencias"
                            )
            return True
        raise Exception(605, "Error de Procesamiento de servicios")
    except Exception as e:
        raise e
