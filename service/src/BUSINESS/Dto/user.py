class UserDto():
    def __init__(self, data):
        self.identification = data.get('identification') or 'NULL'
        self.username = data.get('username') or 'NULL'
        self.surname = data.get('surname') or 'NULL'
        self.lastname = data.get('lastname') or 'NULL'
        self.email = data.get('email') or 'NULL'
        self.phone = data.get('phone') or 'NULL'
        self.state = data.get('state') or 'NULL'
        self.password = data.get('password ') or 'NULL'
        self.nickname = data.get('nickname ') or 'NULL'
