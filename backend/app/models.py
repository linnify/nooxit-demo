from pydantic import BaseModel


class AuthLogin(BaseModel):
    redirect_page: str
