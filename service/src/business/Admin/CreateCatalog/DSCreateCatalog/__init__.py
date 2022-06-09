try:
    __import__("pkg_resources").declare_namespace(__name__)
except ImportError:
    __path__ = __import__("pkgutil").extend_path(__path__, __name__)
from src.infra.web.app.routes import app
from naver_db import NaverDB
from naver_config import NaverConfig
from naver_core import *
import json

config = NaverConfig(app)
nbd = NaverDB(app, config)


def DSCreateCatalog(input):
    try:
        data = input.get("data")
        catalog_id = data.get("catalog_id")
        order = data.get("order")
        description = data.get("description")
        is_active = data.get("is_active")
        code = data.get("code")
        value = json.dumps(data.get("value")).replace("NaN", '""')
        table = "CATALOG_DETAIL"
        schema = "entities"
        stm = f"INSERT INTO {schema}.{table}"
        stm += f"""(catalog_id,
                    "order",
                    description,
                    is_active,
                    code,
                    value
                    )"""
        stm += f""" VALUES ({catalog_id},{order},'{description}',{is_active},{code},\'{value}\')"""
        res = nbd.persistence.setWrite(stm, table)
        return res

    except Exception as e:
        raise e