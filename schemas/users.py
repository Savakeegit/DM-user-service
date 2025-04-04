from pydantic import BaseModel


class UserListSchema(BaseModel):
    id: int
    username: str
    password: str
    telegram_id: str

    class Config:
        from_attributes = True

class UserCreateSchema(BaseModel):
    username: str
    password: str
    telegram_id: str