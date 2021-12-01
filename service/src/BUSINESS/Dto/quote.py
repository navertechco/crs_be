class ItineraryDto():
    def __init__(self, data):
        self.id_intinerary = data.get('id_intinerary') or None
        self.created = data.get('created') or None
        self.updated = data.get('updated') or None
        self.pax = data.get('pax') or 1
        self.id_agent = data.get('id_agent') or None
        self.id_tarvel_expert = data.get('id_tarvel_expert') or None
        self.id_client = data.get('id_client') or None
        self.id_intinerary_state = data.get('id_intinerary_state') or 1
        self.id_country_destination = data.get(
            'id_country_destination') or 1
        self.id_budget = data.get('id_budget') or 1
        self.id_purpose = data.get('id_purpose') or 1
        self.repoductions = data.get('repoductions') or 2

    def __dict__(self):
        return {
            'pax': self.pax,
            'id_agent': self.id_agent,
            'id_tarvel_expert': self.id_tarvel_expert,
            'id_client': self.id_client,
            'id_intinerary_state': self.id_intinerary_state,
            'id_country_destination': self.id_country_destination,
            'id_budget': self.id_budget,
            'id_purpose': self.id_purpose,

        }

    def getAllDict(self):
        return {
            'id_intinerary': self.id_intinerary,
            'created': self.created,
            'updated': self.updated,
            'pax': self.pax,
            'id_agent': self.id_agent,
            'id_tarvel_expert': self.id_tarvel_expert,
            'id_client': self.id_client,
            'id_intinerary_state': self.id_intinerary_state,
            'id_country_destination': self.id_country_destination,
            'id_budget': self.id_budget,
            'id_purpose': self.id_purpose,
            'repoductions': self.repoductions,

        }
