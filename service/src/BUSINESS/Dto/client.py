class ClientDto():
    def __init__(self, data):
        self.id = data.get('id') or 'NULL'
        self.dni = data.get('dni') or 'NULL'
        self.name_contact = data.get('name_contact') or 'NULL'
        self.name_contact_2 = data.get('name_contact_2') or 'NULL' 
        self.address = data.get('address') or 'NULL' 
        self.email = data.get('email') or 'NULL'
        self.phone = data.get('phone') or 'NULL'  
        self.is_owner = data.get('is_owner') or False  
        self.id_client_type = data.get('id_client_type') or 1  
        self.id_legal_client_type = data.get('id_legal_client_type') or 1  
        self.id_origin = data.get('id_origin') or 'US'  
