class ItineraryDayDto():
    def __init__(self, data):
        self.intinerary_id = data.get('intinerary_id') or None
        self.intinerary_day_id = data.get('intinerary_day_id') or None
        self.intinerary_day = data.get('intinerary_day') or None
        self.activity_id = data.get('activity_id') or None
        self.included_option_id = data.get('included_option_id') or None
        self.travel_ritm_id = data.get('travel_ritm_id') or None

    def set(self, attr):
        setattr(self, attr, attr)

    def __dict__(self):
        return {
            "intinerary_id": self.intinerary_id,
            "intinerary_day_id": self.intinerary_day_id,
            "intinerary_day": self.intinerary_day,
            "activity_id": self.activity_id,
            "included_option_id": self.included_option_id,
            "travel_ritm_id": self.travel_ritm_id
        }


class ItineraryDayListDto():
    def __init__(self, data, id):
        self.intinerary_day_list = []
        for d in data:
            intinerary_dayDto = ItineraryDayDto(d) 
            intinerary_dayDto.intinerary_id = id
            self.intinerary_day_list.append(intinerary_dayDto)

    def __dict__(self):
        return {
            "intinerary_day_list": self.intinerary_day_list
        }

    def __list__(self):
        return self.intinerary_day_list
