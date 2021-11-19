class QuoteDayDto():
    def __init__(self, data):
        self.id_quote = data.get('id_quote') or None
        self.id_quote_day = data.get('id_quote_day') or None
        self.quote_day = data.get('quote_day') or None
        self.id_activity = data.get('id_activity') or None
        self.id_included_option = data.get('id_included_option') or None
        self.id_travel_ritm = data.get('id_travel_ritm') or None

    def set(self, attr):
        setattr(self, attr, attr)

    def __dict__(self):
        return {
            "id_quote": self.id_quote,
            "id_quote_day": self.id_quote_day,
            "quote_day": self.quote_day,
            "id_activity": self.id_activity,
            "id_included_option": self.id_included_option,
            "id_travel_ritm": self.id_travel_ritm
        }


class QuoteDayListDto():
    def __init__(self, data, id):
        self.quote_day_list = []
        for d in data:
            quote_dayDto = QuoteDayDto(d) 
            quote_dayDto.id_quote = id
            self.quote_day_list.append(quote_dayDto)

    def __dict__(self):
        return {
            "quote_day_list": self.quote_day_list
        }

    def __list__(self):
        return self.quote_day_list
