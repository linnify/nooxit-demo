from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from ory_hydra_client import ConsentRequest
from starlette import status
from starlette.responses import RedirectResponse
from starlette_wtf import csrf_token, csrf_protect

from app.db import find_by_email
from app.hydra import Hydra

router = APIRouter()
templates = Jinja2Templates("app/templates")
hydra = Hydra()


@router.get("/consent", response_class=HTMLResponse)
async def get_consent(consent_challenge: str, request: Request):
    consent: ConsentRequest = hydra.client.get_consent_request(consent_challenge)

    return templates.TemplateResponse('consent.html', {
        'request': request,
        'challenge': consent_challenge,
        'csrf_token': csrf_token(request),
        'user': consent.subject,
        'client': consent.client,
        'requested_scope': consent.requested_scope,
    })


@router.post('/consent', response_class=HTMLResponse)
@csrf_protect
async def handle_consent(request: Request, challenge: str = Form(...), submit: str = Form(...)):
    consent: ConsentRequest = hydra.client.get_consent_request(challenge)

    if submit == 'cancel':
        # User denied the consent
        redirect_link = hydra.reject_consent(challenge)
        return RedirectResponse(redirect_link, status_code=status.HTTP_303_SEE_OTHER)

    user = find_by_email(consent.subject)
    data = {scope: user[scope] for scope in consent.requested_scope if scope in user}
    
    redirect_url = hydra.accept_consent(consent, data=data)
    return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)
