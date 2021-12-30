try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)

from naver_db import NaverDB
from naver_config import NaverConfig
from naver_core import *
from src.INFRA.WEB.App.routes import app


config = NaverConfig(app)
nbd = NaverDB(app, config)


def DSValidateUser(username):
    try:
        select_stm = "SELECT * "
        from_stm = " FROM entities.user "
        where_stm = " WHERE USERNAME = \'{0}\'".format(username)
        stm = select_stm + from_stm + where_stm
        table = "USER"
        res = nbd.persistence.getQuery(stm, table)
        return res

    except Exception as e:
        raise e
