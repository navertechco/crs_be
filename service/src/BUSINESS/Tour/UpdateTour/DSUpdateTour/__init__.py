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


def DSUpdateTour(input):

    try:
        data = input.get('data')
        tour = TourDto(data).getAllDict()
        table = "TOUR"
        res = nbd.persistence.updateDto(tour, table)
        return res

    except Exception as e:
        raise e
