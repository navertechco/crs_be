class ServiceDto():
    def __init__(self, data):
        self.id_quote_day = data.get('id_quote_day') or None
        self.id_service = data.get('id_service') or None 
        self.id_promo = data.get('id_promo') or None 

    def set(self, attr):
        setattr(self, attr, attr)

    def __dict__(self):
        return {
            "id_quote_day": self.id_quote_day,
            "id_service": self.id_service, 
            "id_promo": self.id_promo 
        }


class ServiceListDto():
    def __init__(self, data, id):
        self.service_list = []
        for d in data['services']:
            serviceDto = ServiceDto(d) 
            serviceDto.id_quote_day = id
            self.service_list.append(serviceDto)

    def __dict__(self):
        return {
            "service_list": self.service_list
        }

    def __list__(self):
        return self.service_list
