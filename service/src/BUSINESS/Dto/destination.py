import json
import ast
import json 
from naver_core import *

 
class DestinationDto():
    def __init__(self, data):
        self.destination_id = data.get("destination_id") or None
        self.created = data.get("created") or None
        self.updated = data.get("updated") or None
        self.port = data.get("port") or None
        self.destination_name = data.get("destination_name") or None
        self.destination_title = data.get("destination_title") or None
        self.hotel_id = data.get("hotel_id") or None
        self.airport_id = data.get("airport_id") or None
        self.has_airport = data.get("has_airport") or False
        self.description = data.get("description") or None
        self.previous = data.get("previous") or None
        self.next = data.get("next") or None
        self.days = json.dumps(prepareJsonData(data.get("days"))) or None

    def set(self, attr):
        setattr(self, attr, attr)

    def __dict__(self):
        return {
            "destination_id": self.destination_id,
            "created": self.created,
            "updated": self.updated,
            "port": self.port,
            "destination_name": self.destination_name,
            "destination_title": self.destination_title,
            "hotel_id": self.hotel_id,
            "airport_id": self.airport_id,
            "has_airport": self.has_airport,
            "description": self.description,
            "previous": self.previous,
            "next": self.next,
            "days": self.days,
        }


class DestinationListDto():
    def __init__(self, data, id):
        self.destination_list = []
        for d in data:
            destinationDto = None
            destinationDto = DestinationDto(d)
            self.destination_list.append(destinationDto.__dict__())

    def __dict__(self):
        return self.destination_list
        

    def __list__(self):
        return self.destination_list
