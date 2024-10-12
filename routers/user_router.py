from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_session
from database.models import User

user_router = APIRouter()


@user_router.get('/get_users')
def get_users(session: Session = Depends(get_session)):
    # Тестовый запрос для проверки работоспособности
    result = session.execute(select(User))
    return {'result': result.all()}


@user_router.get('/get_user/{user_id}')
def get_user(user_id: int):
    pass


@user_router.post('/add_user')
def add_user():
    pass


@user_router.patch('/edit_user/{user_id}')
def edit_user(user_id: int, new_data):
    pass


@user_router.delete('/delete_user/{user_id}')
def delete_user(user_id: int):
    pass
