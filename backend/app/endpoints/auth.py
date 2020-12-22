import json
from typing import Optional

from fastapi import APIRouter, Depends
from starlette.responses import RedirectResponse

from app.config import settings
from app.helpers.deps import get_current_user
from app.helpers.oauth2 import Oauth2Client
from app.models import AuthLogin

router = APIRouter()


@router.post("/auth/login")
async def auth(data: AuthLogin):
    """
    Return SSO Page URL
    """
    state = json.dumps({'success_url': data.redirect_page})
    
    authorize_url = f'{settings.AUTHORIZATION_URL}?response_type=code&response_mode=query'  # noqa
    authorize_url += f'&client_id={settings.CLIENT_ID}'
    authorize_url += f'&redirect_uri={settings.AUTHORIZATION_REDIRECT_URI}'
    authorize_url += f'&state={state}'
    authorize_url += f'&scope=openid email name groups'

    return {
        'authorization_url': authorize_url
    }


@router.get("/auth/callback")
async def auth_callback(state: Optional[str], code: Optional[str] = None, error: Optional[str] = None, error_description: Optional[str] = None):
    data = json.loads(state)
    redirect_url = data.get('success_url')
    
    if error:
        redirect_url += f"?error={error}&error_description={error_description}"
        return RedirectResponse(redirect_url)
    
    token = Oauth2Client().exchange(code)
    access_token = token.get('access_token')
    id_token = token.get('id_token')
    
    # Attach the access token in query params so the client can use it
    redirect_url += f"?token={access_token}&id_token={id_token}"
    return RedirectResponse(redirect_url)


@router.get('/auth/profile')
def auth_profile(user=Depends(get_current_user)):
    return user
