try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)

from src.BUSINESS.Dto import ServiceListDto
from naver_db import NaverDB
from naver_config import NaverConfig
from naver_core import *
from src.WEB.App.routes import app
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
        table = "QUOTE_DAY"
        stm = "SELECT *"
        stm += "FROM {} ".format(table)
        where  = " WHERE ID_QUOTE = \'{}\'".format(id)
        stm += where
        quote_days = nbd.persistence.getQuery(stm, table)
        if len(quote_days) > 0: 
            serviceList = ServiceListDto(quote_days, id).__list__()
            table = "QUOTE_DAY"
            stm = " UPDATE " + table
            stm += " SET services='{}'".format(str(json.dumps({'services': serviceList})))
            where = " WHERE id_quote = \'{}\'".format(id)
            stm += " " + where
            quote_day = nbd.persistence.setWrite(stm, table)
            if len(quote_day) > 0:
                quote_day['session'].commit()
                table= "QUOTE_DAY_DETAILS"
                stm = nbd.persistence.prepareListDtoToInsert(
                    serviceList, table)
                res = nbd.persistence.setWrite(stm, table)
                return res  

    except Exception as e:
        raise e