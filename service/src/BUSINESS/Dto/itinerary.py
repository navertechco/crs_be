class ItineraryDto():
    def __init__(self, data):
        self.intinerary_id = data.get('intinerary_id') or None
        self.created = data.get('created') or None
        self.updated = data.get('updated') or None
        self.pax = data.get('pax') or 1
        self.agent_id = data.get('agent_id') or None
        self.tarvel_expert_id = data.get('tarvel_expert_id') or None
        self.client_id = data.get('client_id') or None
        self.intinerary_state_id = data.get('intinerary_state_id') or 1
        self.country_destination_id = data.get(
            'country_destination_id') or 1
        self.budget_id = data.get('budget_id') or 1
        self.purpose_id = data.get('purpose_id') or 1
        self.repoductions = data.get('repoductions') or 2

    def __dict__(self):
        return {
            'pax': self.pax,
            'agent_id': self.agent_id,
            'tarvel_expert_id': self.tarvel_expert_id,
            'client_id': self.client_id,
            'intinerary_state_id': self.intinerary_state_id,
            'country_destination_id': self.country_destination_id,
            'budget_id': self.budget_id,
            'purpose_id': self.purpose_id,

        }

    def getAllDict(self):
        return {
            'intinerary_id': self.intinerary_id,
            'created': self.created,
            'updated': self.updated,
            'pax': self.pax,
            'agent_id': self.agent_id,
            'tarvel_expert_id': self.tarvel_expert_id,
            'client_id': self.client_id,
            'intinerary_state_id': self.intinerary_state_id,
            'country_destination_id': self.country_destination_id,
            'budget_id': self.budget_id,
            'purpose_id': self.purpose_id,
            'repoductions': self.repoductions,

        }
