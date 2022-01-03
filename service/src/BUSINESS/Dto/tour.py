import json
import ast
import json 
from naver_core import *

 

def findValue(lstdict, key):
    data = [x for x in lstdict if x["code"] == key]
    if len(data) > 0:
        return data[0]["value"]


class TourDto():
    def __init__(self, data):
        client = data.get('client') or None
        tour = data.get('tour') or None
        cover = data.get('cover') or None
        end = data.get('end') or None
        destinations = data.get('destinations') or None
        match = data.get('match') or None
        match_type = data.get('match_type') or None
        details = ({
            "client": client,
            "tour": tour,
            "cover": cover,
            "end": end,
            "destinations": destinations
        })
        self.tour_id = findValue(tour, "tour_id")
        self.created = findValue(tour, "created")
        self.updated = findValue(tour, "updated")
        self.partner = findValue(tour, "partner")
        self.match = match
        self.match_type = match_type
        self.valid = cover.get("valid_until")
        self.destination_country_id = findValue(tour, "country")
        self.purpose_id = findValue(tour, "purpose")
        self.accomodation_type_id = findValue(tour, "accomodation_type")
        self.arrival_date = findValue(tour, "arrival_date")
        self.departure_date = findValue(tour, "departure_date")
        self.contact_agent = findValue(tour, "contact_agent")
        self.pasengers = cover.get("passengers")
        self.days = cover.get("days")
        self.nights = cover.get("nights")
        self.description = cover.get("description")
        self.client_id = findValue(client, "client_id")
        self.detail = json.dumps(prepareJsonData(details))
        self.cover_detail = json.dumps(prepareJsonData(cover))

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
            "cover_detail": self.cover_detail,
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
