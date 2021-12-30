class DayDto():
    def __init__(self, data):
        self.tour_day_id = data.get('tour_day_id') or None
        self.day_id = data.get('day_id') or None 
        self.promo_id = data.get('promo_id') or None 

    def set(self, attr):
        setattr(self, attr, attr)

    def __dict__(self):
        return {
            "tour_day_id": self.tour_day_id,
            "day_id": self.day_id, 
            "promo_id": self.promo_id 
        }


class DayListDto():
    def __init__(self, data):
        self.day_list = []
        for d in data:
            dayDto = DayDto(d) 
            self.day_list.append(dayDto)

    def __dict__(self):
        return {
            "day_list": self.day_list
        }

    def __list__(self):
        return self.day_list
