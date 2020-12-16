from typing import List, Union

from pydantic import BaseSettings, AnyHttpUrl, validator


class Settings(BaseSettings):
    PROJECT_NAME: str = "Nooxit API"

    CLIENT_SECRET: str
    CLIENT_ID: str = 'linnify-app'
    
    AUTHORIZATION_URL: str = 'http://127.0.0.1:5556/dex/auth'
    AUTHORIZATION_TOKEN_URL: str = 'http://127.0.0.1:5556/dex/token'
    AUTHORIZATION_REDIRECT_URI: str = 'http://localhost:8000/auth/callback'
    AUTHORIZATION_USER_INFO_URL: str = 'http://127.0.0.1:5556/dex/userinfo'
    
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)
   
    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
