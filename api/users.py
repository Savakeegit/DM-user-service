from typing import Annotated
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from repositories.users import UserRepository
from schemas.users import UserCreateSchema, UserListSchema
from db.database import get_async_session

router = APIRouter(
    prefix='/users',
    tags=['Пользователи']
)

@router.get('')
async def get_users(session: Annotated[AsyncSession, Depends(get_async_session)], ):
    return {'user_id': 'user_id'}

@router.post('')
async def create_user(user: UserCreateSchema, ):
    user_dict = user.model_dump()
    user_id = await UserRepository().create_one(user_dict)
    return {'user_id': user_id}