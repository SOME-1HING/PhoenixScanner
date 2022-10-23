from requests import get

version = "1.0.0"

class Phoenix():
    def __init__(self):
        self.url = 'https://sheltered-taiga-39139.herokuapp.com/check'

    def gban_check(self, user_id):
        try:
            url = f"{self.url}/{user_id}"
            is_gban = get(url).json()["is_gban"]
            return is_gban
        except:
            pass
