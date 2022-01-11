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


def DSProcessDestinations(tour_id, input):

    try:
        reslist = []
        destinations = getValue(input, 'destinations')
        jsondata = prepareJsonData(destinations)
        destinations = DestinationListDto(jsondata, tour_id).__dict__()
        destinationsToInsert = str(json.dumps(jsondata))
        table = "TOUR"
        schema = "entities"
        stm = " UPDATE " + schema+"."+table
        stm += " SET destinations=\'{}\'".format(destinationsToInsert)
        stm += ", tour_state_id=4"
        where = " WHERE tour_id = \'{}\'".format(tour_id)
        stm += " " + where
        res = nbd.persistence.setWrite(stm, table)
        if len(res) > 0:
            reslist.append(res)
            table = "TOUR_DETAIL"
            for destination in destinations:
                stm = """
                            INSERT INTO {}.{}(TOUR_ID, DETAIL, DESTINATION_ID)
                            VALUES ({},\'{}\',{})
                
                """.format(schema, table, tour_id, str(json.dumps(destination)), destination["destination_id"])
                res = nbd.persistence.setWrite(
                    stm, table)
                if len(res) > 0:
                    reslist.append(res)
        return reslist
    except Exception as e:
        raise e
