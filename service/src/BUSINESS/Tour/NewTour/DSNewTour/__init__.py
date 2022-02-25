try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)

from src.BUSINESS.Dto import TourDto
from src.INFRA.WEB.App.routes import app
from naver_db import NaverDB
from naver_config import NaverConfig
from naver_core import *

config = NaverConfig(app)
nbd = NaverDB(app, config)


def DSNewTour(input):
    """_summary_

    Args:
        input (_type_): _description_

    Raises:
        e: _description_

    Returns:
        _type_: _description_
    """
    try:
        value = getValue(input, 'value')
        tour = TourDto(value)
        data = tour.getAllDict()
        table = "TOUR"
        schema = "entities"
        res = nbd.persistence.insertDto(tour, table, schema)
        return res

    except Exception as e:
        raise e
