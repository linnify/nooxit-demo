from fastapi import Depends
from fastapi.openapi.models import OAuthFlows, OAuthFlowAuthorizationCode
from fastapi.security import OAuth2

from app.config import settings
from app.helpers.dex import Dex

oauth2_scheme = OAuth2(
    flows=OAuthFlows(
        authorizationCode=OAuthFlowAuthorizationCode(
            authorizationUrl=settings.AUTHORIZATION_URL,
            tokenUrl=settings.AUTHORIZATION_TOKEN_URL,
            scopes={
                'openid': 'OpenID',
                'email': 'Email',
                'profile': 'Profile',
                'groups': 'Groups',
                'offline_access': 'Offline Access',
            }
        ),
    )
)


def get_current_user(access_token: str = Depends(oauth2_scheme)):
    """
    Return the current user profile
    :return: current user
    """
    dex_client = Dex()
    user = dex_client.user_profile(access_token)
    return user
