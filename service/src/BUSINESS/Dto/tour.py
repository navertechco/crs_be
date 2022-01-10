import json
import ast
import json 
from naver_core import *

 

def findValue(lstdict, key):
    return lstdict.get(key)


class TourDto():
    def __init__(self, data):
        client = data.get('client') or None
        tour = data.get('tour') or None 
        end = data.get('end') or None
        destinations = data.get('destinations') or None 
        details = ({
            "client": client,
            "tour": tour, 
            "end": end,
            "destinations": destinations
        })
        self.tour_id = findValue(tour, "tour_id")
        self.created = findValue(tour, "created")
        self.updated = findValue(tour, "updated")
        self.partner = findValue(tour, "partner")
        self.match = tour.get("match")
        self.match_type = tour.get("match_type")
        self.valid = tour.get("valid_until")
        self.destination_country_id = findValue(tour, "destination_country_id")
        self.purpose_id = findValue(tour, "purpose_id")
        self.accomodation_type_id = findValue(tour, "accomodation_type_id")
        self.arrival_date = findValue(tour, "arrival_date")
        self.departure_date = findValue(tour, "departure_date")
        self.contact_agent = findValue(tour, "contact_agent")
        self.pasengers = tour.get("passengers")
        self.days = tour.get("days")
        self.nights = tour.get("nights")
        self.description = tour.get("description")
        self.client_id = findValue(client, "client_id")
        self.detail = json.dumps(prepareJsonData(details))
        self.cover_detail = json.dumps( (self.__dict__()))

    def __dict__(self):
        return {

            "partner": self.partner,
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
            "match": self.match,
            "match_type": self.match_type,

        }

    def getAllDict(self):
        return {
            "tour_id": self.tour_id,
            "created": self.created,
            "updated": self.updated,
            "partner": self.partner,
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

        }
