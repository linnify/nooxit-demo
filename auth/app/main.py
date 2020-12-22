import uvicorn
from fastapi import APIRouter, FastAPI
from fastapi.staticfiles import StaticFiles
from starlette import status
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import PlainTextResponse
from starlette_wtf import CSRFProtectMiddleware

from app.config import settings
from app.endpoints import consent
from app.endpoints import login

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(consent.router, tags=["consent"])

app = FastAPI(
    title=settings.PROJECT_NAME,
    middleware=[
        Middleware(SessionMiddleware, secret_key='***REPLACEME1***'),
        Middleware(CSRFProtectMiddleware, enabled=True, csrf_secret='csrf_secret',)
    ]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.exception_handler(Exception)
async def exception_handler(request, exc):
    # TODO Response with a custom HTML
    return PlainTextResponse(str(exc), status_code=status.HTTP_400_BAD_REQUEST)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)
