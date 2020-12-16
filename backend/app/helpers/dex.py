import requests

from app.config import settings


class Dex:
    
    def __init__(
        self,
        token_type='bearer',
    ):
        self.client_id = settings.CLIENT_ID
        self.client_secret = settings.CLIENT_SECRET
        self.token_type = token_type
        
        super().__init__()
    
    def exchange(self, code: str):
        """
        Exchange code for an Access Token and ID Token
        :param code:
        :return:
        """
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': settings.AUTHORIZATION_REDIRECT_URI
        }
        
        response = requests.post(settings.AUTHORIZATION_TOKEN_URL, data=data)
        response.raise_for_status()
        
        return response.json()
    
    def user_profile(self, token: str):
        headers = {'Authorization': f'{self.token_type} {token}'}
        response = requests.get(settings.AUTHORIZATION_USER_INFO_URL, headers=headers)
        response.raise_for_status()
        
        return response.json()

