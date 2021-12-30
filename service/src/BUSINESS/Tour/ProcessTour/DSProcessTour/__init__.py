try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)

from naver_db import NaverDB
from naver_config import NaverConfig
from naver_core import *
from src.INFRA.WEB.App.routes import app 


config = NaverConfig(app)
nbd = NaverDB(app,config)

def DSProcessTour(id):
    """Método para validar si existe una cotización

    Args:
        id (int): id de la cotización

    Raises:
        e: Error de conexión a la base de datos

    Returns:
        res: Resultado de la consulta
    """       
    try:
        table = "ITINERARY"
        stm = " UPDATE "
        stm += table 
        stm += " SET ID_ITINERARY_STATE = 2 "
        stm += " WHERE itinerary_id = \'{}\'".format(id)
        stm += " AND itinerary_state_id >= 1"
        res = nbd.persistence.setWrite(stm, table)
        return res  

    except Exception as e:
        raise e