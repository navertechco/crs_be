try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)

from src.BUSINESS.Dto import QuoteDto
from src.WEB.App.routes import app
from naver_db import NaverDB
from naver_config import NaverConfig
from naver_core import *

config = NaverConfig(app)
nbd = NaverDB(app, config)


def DSUpdateQuote(input):

    try:
        data = input.get('data')
        quote = QuoteDto(data).getAllDict()
        table = "QUOTE"
        res = nbd.persistence.updateDto(quote, table)
        return res

    except Exception as e:
        raise e
