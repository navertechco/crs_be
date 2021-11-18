try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)

from src.BUSINESS.Dto import DestinationListDto
from naver_db import NaverDB
from naver_config import NaverConfig
from naver_core import *
from src.WEB.App.routes import app


config = NaverConfig(app)
nbd = NaverDB(app, config)


def DSProcessDestinations(id, input):

    try:
        destinations = getValue(input, 'destinations')
        destinationList = DestinationListDto(destinations, id).__list__()
        table = "QUOTE_DAY"       
        stm = nbd.persistence.prepareListDtoToInsert(
            destinationList, table)        
        res = nbd.persistence.setWrite(stm, table)
        return res
    except Exception as e:
        raise e
