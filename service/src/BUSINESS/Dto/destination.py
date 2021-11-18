class DestinationDto():
    def __init__(self, data):
        self.id_quote = data.get('id_quote') or None
        self.id_destination = data.get('id_destination') or None
        self.quote_day = data.get('quote_day') or None
        self.id_activity = data.get('id_activity') or None
        self.id_included_option = data.get('id_included_option') or None
        self.id_travel_ritm = data.get('id_travel_ritm') or None

    def set(self, attr):
        setattr(self, attr, attr)

    def __dict__(self):
        return {
            "id_quote": self.id_quote,
            "id_destination": self.id_destination,
            "quote_day": self.quote_day,
            "id_activity": self.id_activity,
            "id_included_option": self.id_included_option,
            "id_travel_ritm": self.id_travel_ritm
        }


class DestinationListDto():
    def __init__(self, data, id):
        self.destination_list = []
        for d in data:
            destinationDto = DestinationDto(d) 
            destinationDto.id_quote = id
            self.destination_list.append(destinationDto)

    def __dict__(self):
        return {
            "destination_list": self.destination_list
        }

    def __list__(self):
        return self.destination_list
