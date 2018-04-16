import requests
from enum import Enum
from base64 import b64decode

__all__ = ['Category', 'Trivia']

categories = {}
for a in requests.get('https://opentdb.com/api_category.php').json()['trivia_categories']:
    categories[a['name']] = a['id']
Category = Enum('Category', categories)

class Trivia:
    def __init__(self):
        self.token_id = requests.get('https://opentdb.com/api_token.php', params={'command':'request'}).json()['token']
    def getquestion(self, category=None, difficulty=None, type=None, amount=1):
        obj = {k: v for k, v in locals().items() if v is not None}
        obj.update({'token':self.token_id, 'encode':'base64'})
        del obj['self']
        response = requests.get('https://opentdb.com/api.php', params=obj).json()
        if response['response_code'] == 0:
            return list({k: (list(b64decode(n).decode('utf-8') for n in v) if isinstance(v, list) else b64decode(v).decode('utf-8')) for k, v in x.items()} for x in response["results"])
        elif response['response_code'] == 1:
            return 'No results'
        elif response['response_code'] == 2:
            return 'Invalid Parameter'
        elif response['response_code'] == 3:
            self.token_id = requests.get('https://opentdb.com/api_token.php', params={'command':'request'}).json()['token']
            return self.getquestion(category=category, difficulty=difficulty, type=type, amount=amount)
        elif response['response_code'] == 4:
            self.token_id = requests.get('https://opentdb.com/api_token.php', params={'command':'reset', 'token':self.token_id}).json()['token']
            return self.getquestion(category=category, difficulty=difficulty, type=type, amount=amount)
