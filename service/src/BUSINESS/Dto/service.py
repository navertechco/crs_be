class ServiceDto():
    def __init__(self, data):
        self.intinerary_day_id = data.get('intinerary_day_id') or None
        self.service_id = data.get('service_id') or None 
        self.promo_id = data.get('promo_id') or None 

    def set(self, attr):
        setattr(self, attr, attr)

    def __dict__(self):
        return {
            "intinerary_day_id": self.intinerary_day_id,
            "service_id": self.service_id, 
            "promo_id": self.promo_id 
        }


class ServiceListDto():
    def __init__(self, data):
        self.service_list = []
        for d in data:
            serviceDto = ServiceDto(d) 
            self.service_list.append(serviceDto)

    def __dict__(self):
        return {
            "service_list": self.service_list
        }

    def __list__(self):
        return self.service_list
