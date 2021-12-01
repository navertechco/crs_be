class ItineraryDayDto():
    def __init__(self, data):
        self.itinerary_id = data.get('itinerary_id') or None
        self.itinerary_day_id = data.get('itinerary_day_id') or None
        self.itinerary_day = data.get('itinerary_day') or None
        self.activity_id = data.get('activity_id') or None
        self.included_option_id = data.get('included_option_id') or None
        self.travel_ritm_id = data.get('travel_ritm_id') or None

    def set(self, attr):
        setattr(self, attr, attr)

    def __dict__(self):
        return {
            "itinerary_id": self.itinerary_id,
            "itinerary_day_id": self.itinerary_day_id,
            "itinerary_day": self.itinerary_day,
            "activity_id": self.activity_id,
            "included_option_id": self.included_option_id,
            "travel_ritm_id": self.travel_ritm_id
        }


class ItineraryDayListDto():
    def __init__(self, data, id):
        self.itinerary_day_list = []
        for d in data:
            itinerary_dayDto = ItineraryDayDto(d) 
            itinerary_dayDto.itinerary_id = id
            self.itinerary_day_list.append(itinerary_dayDto)

    def __dict__(self):
        return {
            "itinerary_day_list": self.itinerary_day_list
        }

    def __list__(self):
        return self.itinerary_day_list
