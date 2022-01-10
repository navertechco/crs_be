try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSProcessTour import DSProcessTour
from ...NewMatch import NewMatch
from ...ProcessDestinations import ProcessDestinations
from ...ProcessDays import ProcessDays 
from src.BUSINESS.System.GetNextVal import GetNextVal
from naver_core import *


def BSProcessTour(tour_id, input):
    """Método de Procesamiento Tour

    Args:
        tour_id (int): Identificador de Tour
        input (dict): Diccionario con los datos de Tour

    Raises:
        Exception: Cuando no se puede procesar Tour
        Exception: Cuando no se puede procesar los destinos
        Exception: Cuando no se puede procesar los días
        Exception: Cuando no se puede crear el Match
        e: Todas las expeciones

    Returns:
        bool: [description]
    """
    try:
        def finalProccess():
            processed = DSProcessTour(tour_id)
            if len(processed) > 0:
                processed["session"].commit()
                return True
            raise Exception( 605, "Error de Procesamiento de tour")
        data = input.get('data')
        destinations = data.get('destinations')
        tour = data.get('tour')
        match = tour.get('match')
        if match is not None:
            if destinations is not None:
                match = NewMatch().BSNewMatch(tour_id, input)
                if len(match) > 0:
                    match["session"].commit()
                    destinations_res = ProcessDestinations().BSProcessDestinations(tour_id, input)
                    if len(destinations_res) > 0:
                        index = 0
                        destination_indexes = []
                        for destination_res in destinations_res:
                            destination_res["session"].commit()
                            last_row_id = GetNextVal().BSGetNextVal("TOUR_DETAIL", "tour_detail_id")-len(destinations_res)+1+index
                            if index > 0:
                                destination_indexes.append(last_row_id)
                            index+=1
                        for destination in destinations:
                            destination_index = destination_indexes[0]
                            destination["tour_detail_id"] = destination_index
                            days = ProcessDays().BSProcessDays(tour_id, destination)
                            if days is False:
                                raise Exception(605, "Error de Procesamiento de días")
                        return finalProccess()
                    raise Exception(605, "Error de Procesamiento de destinos")
                raise Exception(605, 'Error de Procesamiento de match')
            raise Exception(605, 'No tiene destinos el tour')
        raise Exception(605, 'No tiene match el tour')
    except Exception as e:
        raise e
