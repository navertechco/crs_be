try:
    __import__("pkg_resources").declare_namespace(__name__)
except ImportError:
    __path__ = __import__("pkgutil").extend_path(__path__, __name__)

from naver_db import NaverDB
from naver_config import NaverConfig
from naver_core import *
from src.infra.web.app.routes import app


config = NaverConfig(app)
nbd = NaverDB(app, config)


def DSFindCruise(input):
    """_summary_

    Args:
        input (_type_): _description_

    Raises:
        e: _description_

    Returns:
        _type_: _description_
    """
    try:
        cruise_id = getValue(input, "cruise_id")
        table = "cruise"
        schema = "entities"
        stm = " SELECT t.* "
        stm += f" FROM {schema}.{table} t"

        if cruise_id != 0:
            stm += f" WHERE cruise_id='{cruise_id}'"

        stm += "  ORDER BY t.cruise_id DESC"
        res = nbd.persistence.getQuery(stm, table)
        return res

    except Exception as e:
        raise e