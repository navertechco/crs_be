from naver_core import utils


class ProfileDto():
    def __init__(self, data):
        try:
            self.username = utils.replaceDictIf(data, 'username', 'NULL')
            self.surname = utils.replaceDictIf(data, 'surname', 'NULL')
            self.nickname = utils.replaceDictIf(data, 'nickname', 'NULL')
            self.lastname = utils.replaceDictIf(data, 'lastname', 'NULL')
            self.email = utils.replaceDictIf(data, 'email', 'NULL')
            self.phone = utils.replaceDictIf(data, 'phone', 'NULL')
            self.state = utils.replaceDictIf(data, 'state', 'NULL')
            self.credits = utils.replaceDictIf(data, 'credits', 'NULL')
            self.identification = utils.replaceDictIf(data, 'identification', 'NULL')
            self.avatar = utils.replaceDictIf(data, 'avatar', 'NULL')
        except Exception as e:
            raise e

    def __dict__(self):
        return {
            'username': self.username,
            'surname': self.surname,
            'credits': self.credits,
            'nickname': utils.replaceIf(self.nickname, 'None', None),
            'lastname': self.lastname,
            'email': self.email,
            'phone': self.phone,
            'state': self.state,
            'identification': self.identification,
            'avatar': self.avatar
        }
