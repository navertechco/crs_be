import os
import json
import pandas as pd
import requests
# from src.infra.web.app.libs import app


class CruiseDto(object):
    def __init__(self, **kwargs):
        self.cruise_id = kwargs.get("cruise_id") or 0
        self.cruise_name = kwargs.get("cruise_name")
        self.cruise_type = kwargs.get("cruise_type")
        self.cruise_category = kwargs.get("cruise_category")
        self.description = kwargs.get("description")
        self.armor_name = kwargs.get("armor_name")
        self.operator_name = kwargs.get("operator_name")
        self.comercial_name = kwargs.get("comercial_name")
        self.arrival_port = kwargs.get("arrival_port")
        self.modality = kwargs.get("modality")
        self.pax = kwargs.get("pax")
        self.web_page = kwargs.get("web_page")
        self.included = kwargs.get("included")
        self.information = kwargs.get("information")
        self.guide_number = kwargs.get("guide_number")
        self.staff_number = kwargs.get("staff_number")
        self.medic = kwargs.get("medic")
        self.tc = kwargs.get("tc")
        self.internet = kwargs.get("internet")
        self.wetsuites = kwargs.get("wetsuites")
        self.aditional_services = kwargs.get("aditional_services")
        self.restrictions = kwargs.get("restrictions")
        self.cruise_format = kwargs.get("cruise_format")
        self.cruise_itinerary = kwargs.get("cruise_itinerary")


class CruiseDetailDto(object):
    def __init__(self, **kwargs):
        self.cruise_detail_id = kwargs.get("cruise_detail_id") or 0
        self.cruise_id = kwargs.get("cruise_id")
        self.cruise_name = kwargs.get("cruise_name")
        self.cabine_type = kwargs.get("cabine_type")
        self.cabine_spec = kwargs.get("cabine_spec")
        self.quantity = kwargs.get("quantity")
        self.net_rate = kwargs.get("net_rate")


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_PATH = os.path.join(ROOT_DIR, "import\\cruises.xlsx")


cruise = pd.read_excel(FILE_PATH, sheet_name="CRUISE")
cruise_detail = pd.read_excel(FILE_PATH,   sheet_name="CRUISE_DETAIL")
# print(cruise.head(10))
print(cruise.head(10).to_json(orient="records"))
