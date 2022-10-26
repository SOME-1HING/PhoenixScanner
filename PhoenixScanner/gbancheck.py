from requests import get

class Phoenix():
    def __init__(self):
        self.url = 'https://sheltered-taiga-39139.herokuapp.com/check'

    def gban_check(self, user_id):
        try:
            url = f"{self.url}/{user_id}"
            is_gban = get(url).json()["is_gban"]
            reason = get(url).json()["reason"]
            scanner = get(url).json()["scanner"]
            return is_gban, reason, scanner
        except:
            pass
 