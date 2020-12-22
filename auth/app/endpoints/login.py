from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette import status
from starlette.responses import RedirectResponse
from starlette_wtf import csrf_protect, csrf_token

from app.hydra import Hydra
from app.db import find_by_email_and_password

router = APIRouter()
templates = Jinja2Templates("app/templates")
hydra = Hydra()


@router.get("/login", response_class=HTMLResponse)
def login(login_challenge: str, request: Request):
    login_request = hydra.get_login_request(login_challenge)
    
    return templates.TemplateResponse('login.html', {
        'request': request,
        'challenge': login_challenge,
        'csrf_token': csrf_token(request),
        'hint': login_request.oidc_context.login_hint or '',
    })


@router.post('/login', response_class=HTMLResponse)
@csrf_protect
async def handle_login(request: Request, challenge: str = Form(...)):
    
    form_data = await request.form()
    email = form_data.get('email')
    password = form_data.get('password')
    submit = form_data.get('submit')
    
    if submit == 'cancel':
        # User denied the login
        redirect_login = hydra.reject_login(challenge)
        return RedirectResponse(redirect_login, status_code=status.HTTP_303_SEE_OTHER)
    
    user = find_by_email_and_password(email, password)
    
    if not user:
        return templates.TemplateResponse('login.html', {
            'request': request,
            'challenge': challenge,
            'csrf_token': csrf_token(request),
            'error': 'The email / password combination is not correct'
        })
    
    redirect_url = hydra.accept_login_request(challenge, email)
    return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)
