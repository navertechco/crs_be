try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from src.BUSINESS.Dto import ClientDto
from src.INFRA.WEB.App.routes import app
from naver_db import NaverDB
from naver_config import NaverConfig
from naver_core import *

config = NaverConfig(app)
nbd = NaverDB(app, config)


def DSGetDestination(destination_id):
    try:
        where = "where destination_id = \'{}\'".format(destination_id)
        if destination_id == "ALL":
            where = ""
        table = "DESTINATION"
        stm = "select * from entities.destination {}".format(where)
        res = nbd.persistence.getQuery(stm, table) 
        return res
    except Exception as e:
        raise e
