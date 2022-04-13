import json
import ast
import json
from naver_core import *


class TourDto():
    def __init__(self, value):
        #from Frontend
        tour = value.get('tour') or None
        logistic = value.get('logistic') or None
        customer = value.get('customer') or None 
        promoted = value.get('promoted') or None
        destinations = value.get('destinations') or None
        day = promoted.get('day') or None

        #to DataBase
        self.tour_id = tour.get("tour_id")
        self.created = tour.get("created")
        self.updated = tour.get("updated") 
        self.match = tour.get("match")
        self.match_type = tour.get("match_type")
        self.destinations = json.dumps(destinations)
        self.valid = tour.get("valid_until")
        self.destination_country_id = tour.get("country")
        self.purpose_id = tour.get("purpose")
        self.accomodation_type_id = tour.get("accomodation_type")
        self.arrival_date = logistic.get("arrival_date")
        self.departure_date = logistic.get("departure_date")
        self.contact_agent = tour.get("contact_agent")
        self.pasengers = tour.get("passengers")
        self.days = len(day) - 1
        self.nights = self.days - 1
        self.description = customer.get("travel_code")
        self.client_id = int(customer.get("dni"))
        self.detail =  json.dumps(self.__dict__(), indent=4, sort_keys=True, default=str)

    #to DataBase
    def __dict__(self):
        return {

 
            "valid": self.valid,
            "destination_country_id": self.destination_country_id,
            "purpose_id": self.purpose_id,
            "accomodation_type_id": self.accomodation_type_id,
            "arrival_date": self.arrival_date,
            "departure_date": self.departure_date,
            "contact_agent": self.contact_agent,
            "pasengers": self.pasengers,
            "days": self.days,
            "nights": self.nights,
            "description": self.description,
            "client_id": self.client_id,
            "match": self.match,
            "match_type": self.match_type,
            "destinations": self.destinations,
            

        }

    #from DataBase
    def getAllDict(self):
        return {
            "tour_id": self.tour_id,
            "created": self.created,
            "updated": self.updated, 
            "valid": self.valid,
            "destination_country_id": self.destination_country_id,
            "purpose_id": self.purpose_id,
            "accomodation_type_id": self.accomodation_type_id,
            "arrival_date": self.arrival_date,
            "departure_date": self.departure_date,
            "contact_agent": self.contact_agent,
            "pasengers": self.pasengers,
            "days": self.days,
            "nights": self.nights,
            "description": self.description,
            "client_id": self.client_id,
            "detail": self.detail,
            "cover_detail": self.cover_detail,
            "match": self.match,
            "match_type": self.match_type,
            "destinations": self.destinations,

        }
