from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_session
from database.repositories import UserRepository
from schemas.user_schemas import UserCreate, UserReturn, UserEdit
from utils.order_converter import convert_orders

user_router = APIRouter(prefix='/user')


def get_user_repo(session: Session = Depends(get_session)):
    return UserRepository(session)


@user_router.get('/get_users', response_model=List[UserReturn])
def get_users(repo: UserRepository = Depends(get_user_repo)):
    result = repo.get_users()
    out = list()
    for item in result:
        orders = convert_orders(item.orders)

        out.append(UserReturn(id=item.id, name=item.name, orders=orders))
    return out


@user_router.get('/get_user/{user_id}', response_model=UserReturn)
def get_user_by_id(user_id: int, repo: UserRepository = Depends(get_user_repo)):
    result = repo.get_user_by_id(user_id)
    if result:
        orders = convert_orders(result.orders)
        return UserReturn(id=result.id, name=result.name, orders=orders)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No user with id={user_id} found.')


@user_router.post('/add_user', response_model=UserReturn)
def add_user(user_data: UserCreate, repo: UserRepository = Depends(get_user_repo)):
    result = repo.create_user(user_data)
    return UserReturn(id=result.id, name=result.name)


@user_router.patch('/edit_user/{user_id}', response_model=UserReturn)
def edit_user(user_id: int, new_data: UserEdit, repo: UserRepository = Depends(get_user_repo)):
    result = repo.update_user_by_id(user_id, new_data)
    if result is not None:
        orders = convert_orders(result.orders)
        return UserReturn(id=result.id, name=result.name, orders=orders)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No user with id={user_id} found.')


@user_router.delete('/delete_user/{user_id}', response_model=int)
def delete_user(user_id: int, repo: UserRepository = Depends(get_user_repo)):
    result = repo.delete_user_by_id(user_id)
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No user with id={user_id} found.')
    if type(result) is str:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=result)
    return status.HTTP_200_OK
