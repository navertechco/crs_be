
import pandas as pd
import os
from naver_db import NaverDB
from naver_config import NaverConfig
from naver_core import *
any_module(__file__, 3)
from src.infra.web.app.routes import app

config = NaverConfig(app)
nbd = NaverDB(app, config)

# import_excel_to_db(__file__, "cruises.xlsx", "CRUISE", "CRUISE", nbd, False)
# import_excel_to_db(__file__, "cruises.xlsx", "CRUISE_DETAIL", "CRUISE_DETAIL", nbd, False)
