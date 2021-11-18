class QuoteDto():
    def __init__(self, data):
        self.id_quote=data.get('id_quote') or 'NULL'
        self.created=data.get('created') or 'NULL'
        self.updated=data.get('updated') or 'NULL'
        self.pax=data.get('pax') or 'NULL'
        self.id_agent=data.get('id_agent') or 'NULL'
        self.id_tarvel_expert=data.get('id_tarvel_expert') or 'NULL'
        self.id_client=data.get('id_client') or 'NULL'
        self.id_quote_state=data.get('id_quote_state') or 'NULL'
        self.id_country_destination=data.get('id_country_destination') or 'NULL'
        self.id_budget=data.get('id_budget') or 'NULL'
        self.id_purpose=data.get('id_purpose') or 'NULL'
        self.repoductions=data.get('repoductions') or 'NULL' 
    def __dict__(self):
        return {
            'pax': self.pax,
            'id_agent': self.id_agent,
            'id_tarvel_expert': self.id_tarvel_expert,
            'id_client': self.id_client,
            'id_quote_state': self.id_quote_state,
            'id_country_destination': self.id_country_destination,
        }
 