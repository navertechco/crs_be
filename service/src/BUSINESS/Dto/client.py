class ClientDto():
    def __init__(self, data):
     
        self.dni = data.get('dni') or 'NULL'
        self.name_contact = data.get('name_contact') or 'NULL'
        self.name_contact_2 = data.get('name_contact_2') or 'NULL' 
        self.address = data.get('address') or 'NULL' 
        self.email = data.get('email') or 'NULL'
        self.phone = data.get('phone') or 'NULL'  
        self.is_owner = data.get('is_owner') or False  
        self.client_type_id = data.get('client_type_id') or 1  
        self.legal_client_type_id = data.get('legal_client_type_id') or 1  
        self.origin_id = data.get('origin_id') or 'US'  
    def __dict__(self):
        return {
           
            'dni': self.dni,
            'name_contact': self.name_contact,
            'name_contact_2': self.name_contact_2,
            'address': self.address,
            'email': self.email,
            'phone': self.phone,
            'is_owner': self.is_owner,
            'client_type_id': self.client_type_id,
            'legal_client_type_id': self.legal_client_type_id,
            'origin_id': self.origin_id
        }