class DestinationDto():
    def __init__(self, data):
        self.intinerary_id = data.get('intinerary_id') or None
        self.destination_id = data.get('destination_id') or None
        self.intinerary_day = data.get('intinerary_day') or None
        self.activity_id = data.get('activity_id') or None
        self.included_option_id = data.get('included_option_id') or None
        self.travel_ritm_id = data.get('travel_ritm_id') or None

    def set(self, attr):
        setattr(self, attr, attr)

    def __dict__(self):
        return {
            "intinerary_id": self.intinerary_id,
            "destination_id": self.destination_id,
            "intinerary_day": self.intinerary_day,
            "activity_id": self.activity_id,
            "included_option_id": self.included_option_id,
            "travel_ritm_id": self.travel_ritm_id
        }


class DestinationListDto():
    def __init__(self, data, id):
        self.destination_list = []
        for d in data['destinations']:
            destinationDto = DestinationDto(d) 
            destinationDto.intinerary_id = id
            self.destination_list.append(destinationDto)

    def __dict__(self):
        return {
            "destination_list": self.destination_list
        }

    def __list__(self):
        return self.destination_list
