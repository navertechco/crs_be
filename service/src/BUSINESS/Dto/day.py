import json
class DayDto():
    def __init__(self, data): 
        self.day_id=data.get('day_id') or None
        self.created=data.get('created') or None
        self.updated=data.get('updated') or None
        self.key_activity_id=data.get('key_activity_id') or None
        self.day_name=data.get('day_name') or None
        self.day_description=data.get('day_description') or None
        self.day_previous=data.get('day_previous') or None
        self.experiences=json.dumps(data.get('experiences')) or None
        self.description=data.get('description') or None
        self.transport_id=data.get('transport_id') or None
        self.day_observation=data.get('day_observation') or None
        self.day_next=data.get('day_next') or None
        self.meals=data.get('meals') or None
        self.tour_detail_id=data.get('tour_detail_id') or None
        self.props=data.get('props') or None

    def set(self, key, value):
        """Setter

        Args:
            key (str): Key
            value (Any): Value
        """        
        setattr(self, key, value)

    def __dict__(self):
        return {
            "day_id":self.day_id,
            "created":self.created,
            "updated":self.updated,
            "key_activity_id":self.key_activity_id,
            "day_name":self.day_name,
            "day_description":self.day_description,
            "day_previous":self.day_previous,
            "experiences":self.experiences,
            "description":self.description,
            "transport_id":self.transport_id,
            "day_observation":self.day_observation,
            "day_next":self.day_next,
            "meals":self.meals,
            "tour_detail_id":self.tour_detail_id,
            "props":self.props,
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
