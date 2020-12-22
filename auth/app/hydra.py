from ory_hydra_client import Configuration, ApiClient, AdminApi, LoginRequest, \
    CompletedRequest, ConsentRequest

from app.config import settings


class Hydra:
    
    def __init__(self):
        configuration = Configuration(host=settings.HYDRA_ADMIN_URL)
        client = ApiClient(configuration=configuration)
        self.client = AdminApi(api_client=client)
    
    def get_login_request(self, challenge) -> LoginRequest:
        return self.client.get_login_request(challenge)
    
    def reject_login(self, challenge):
        body = {
            'error': 'access_denied',
            'error_description': 'The resource owner denied the request'
        }
        data: CompletedRequest = self.client.reject_login_request(challenge, body=body)
        return data.redirect_to
    
    def reject_consent(self, challenge) -> str:
        body = {
            'error': 'scoped_denied',
            'error_description': 'The resource owner denied the scope'
        }
        data = self.client.reject_consent_request(challenge, body=body)
        return data.redirect_to
    
    def accept_login_request(self, challenge: str, email: str) -> str:
        
        login_request = self.get_login_request(challenge)
        acr_values = login_request.oidc_context.acr_values
        acr_values = acr_values[-1] if acr_values and len(acr_values) > 1 else '0'
        
        body = {
            'subject': email,
            'remember': False,
            'acr': acr_values
        }
        data: CompletedRequest = self.client.accept_login_request(
            challenge,
            body=body
        )
        
        return data.redirect_to
    
    def accept_consent(self, consent: ConsentRequest, data: dict):
        data['email'] = consent.subject
        body = {
            'grant_scope': consent.requested_scope,
            'grant_access_token_audience': consent.requested_access_token_audience,
            'session': {
                'id_token': data
            }
        }
    
        response = self.client.accept_consent_request(consent.challenge, body=body)
        return response.redirect_to
