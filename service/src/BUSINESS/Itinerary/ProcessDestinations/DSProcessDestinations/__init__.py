try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)

from src.BUSINESS.Dto import DestinationListDto
from naver_db import NaverDB
from naver_config import NaverConfig
from naver_core import *
from src.INFRA.WEB.App.routes import app
import ast
import json

config = NaverConfig(app)
nbd = NaverDB(app, config)


def DSProcessDestinations(id, input):

    try:
        destinations = {'destinations': getValue(input, 'destinations')}
        jsondata = (ast.literal_eval(jsonConvert(str(destinations).replace("'", '"'))))
        destinationList = DestinationListDto(jsondata, id).__list__()
        table = "QUOTE"
        stm = " UPDATE " + table
        stm += " SET destinations='{}'".format(str(json.dumps(jsondata)))
        stm += ", id_intinerary_state=4"
        where = " WHERE id_intinerary = \'{}\'".format(id)
        stm += " " + where
        res = nbd.persistence.setWrite(stm, table)
        if len(res) > 0:
            res['session'].commit()
            table = "QUOTE_DAY"
            stm = nbd.persistence.prepareListDtoToInsert(
                destinationList, table)
            res = nbd.persistence.setWrite(stm, table)
            return res
    except Exception as e:
        raise e
