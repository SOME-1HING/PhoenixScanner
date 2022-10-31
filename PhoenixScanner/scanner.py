import json
from requests import get, put

class Phoenix():
    def __init__(self, token):
        self.url = 'https://phoenixscanner-api.some-1hing.repl.co'
        self.token = token
    
    def check(self, user_id):
        try:
            url = f"{self.url}/gban/check/{user_id}?TOKEN={self.token}"
            '''if msg := get(url).json()["message"]:
                return msg'''
            try:
                return get(url).json()['message']
            except:
                return {
                    "user_id": int(user_id),
                    "is_gban": bool(get(url).json()["is_gban"]),
                    "reason": get(url).json()["reason"],
                    "scanner": get(url).json()["scanner"],
                }

        except Exception as e:
            return e
        
    def revert(self, user_id):
        try:
            url = f"{self.url}/gban/revert/{user_id}?TOKEN={self.token}"
            return get(url).json()["message"]
        except:
            pass
        
    def scan(self, user_id, reason, scannedBy):
        try:
            scan = {
                "user_id": int(user_id),
                "reason": reason,
                "scanner": int(scannedBy)
            }
            url = f"{self.url}/gban/scan/?TOKEN={self.token}"
            return put(
                url,
                data=json.dumps(scan),
                headers={"Content-Type": "application/json"},
            ).json()['message']

        except:
            pass
        
    def scanlist(self):
        try:
            url = f"{self.url}/gban/scanlist/?TOKEN={self.token}"
            scanlist = get(url).json()
            return scanlist
        except:
            pass
            
    def token_gen(self):
        try:
            url = f"{self.url}/token/tokengen?TOKEN={self.token}"
            try:
                return get(url).json()['message']
            except:
                token = get(url).json()["token"]
                return token
        except:
            pass
        
    def token_revoke(self, token):
        try:
            url = f"{self.url}/token/revoke/{token}?TOKEN={self.token}"
            return get(url).json()["message"]
        except:
            pass