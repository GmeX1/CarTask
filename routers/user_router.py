from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_session
from database.models import User
from schemas.user_schemas import UserCreate, UserReturn

user_router = APIRouter()


@user_router.get('/get_users')
def get_users(session: Session = Depends(get_session)):
    # Тестовый запрос для проверки работоспособности
    result = session.execute(select(User)).all()
    out = list()
    for item in result:
        print(item.orders)
        out.append(UserReturn(id=item.id, name=item.name))
    return out


@user_router.get('/get_user/{user_id}')
def get_user(user_id: int):
    pass


@user_router.post('/add_user')  # Как работает orders?
def add_user(user_data: UserCreate, session: Session = Depends(get_session)):
    new_user = User(name=user_data.name)
    session.add(new_user)
    session.commit()
    return UserReturn(id=new_user.id, name=new_user.name)


@user_router.patch('/edit_user/{user_id}')
def edit_user(user_id: int, new_data):
    pass


@user_router.delete('/delete_user/{user_id}')
def delete_user(user_id: int):
    pass
