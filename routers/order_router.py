from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from database import get_session
from database.repositories import OrderRepository
from schemas.order_schemas import OrderCreate, OrderReturn, OrderEdit

order_router = APIRouter(prefix='/order')


def get_order_repo(session: Session = Depends(get_session)):
    return OrderRepository(session)


@order_router.get('/get_orders', response_model=List[OrderReturn])
def get_orders(repo: OrderRepository = Depends(get_order_repo)):
    result = repo.get_orders()
    out = list()
    for item in result:
        out.append(OrderReturn(
            id=item.id,
            creation_date=item.creation_date,
            user_id=item.user_id,
            car_id=item.car_id
        ))
    return out


@order_router.get('/get_orders_user/{user_id}', response_model=List[OrderReturn])
def get_orders_by_user_id(user_id: int, repo: OrderRepository = Depends(get_order_repo)):
    result = repo.get_orders_by_user_id(user_id)

    out = list()
    for item in result:
        out.append(OrderReturn(
            id=item.id,
            creation_date=item.creation_date,
            user_id=item.user_id,
            car_id=item.car_id
        ))
    return out


@order_router.post('/add_order', response_model=OrderReturn)
def add_order(order_data: OrderCreate, repo: OrderRepository = Depends(get_order_repo)):
    new_order = repo.create_order(order_data)
    if type(new_order) is str:
        return HTTPException(status_code=status.HTTP_409_CONFLICT, detail=new_order)
    return OrderReturn(
        id=new_order.id,
        creation_date=new_order.creation_date,
        user_id=new_order.user_id,
        car_id=new_order.car_id
    )


@order_router.patch('/edit_order/{order_id}', response_model=OrderReturn)
def edit_order(order_id: int, new_data: OrderEdit, repo: OrderRepository = Depends(get_order_repo)):
    result = repo.edit_order_by_order_id(order_id, new_data)
    if type(result) is str:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=result)
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No order with order_id={order_id} found.')
    return OrderReturn(
        id=result.id,
        creation_date=result.creation_date,
        user_id=result.user_id,
        car_id=result.car_id
    )


@order_router.delete('/delete_orders_by_user_id/{user_id}', response_model=int)
def delete_orders_by_user_id(user_id: int, repo: OrderRepository = Depends(get_order_repo)):
    result = repo.delete_orders_by_user_id(user_id)
    if type(result) is str:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=result)
    if result:
        return status.HTTP_200_OK
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No order with user_id={user_id} found.')


@order_router.delete('/delete_order_by_order_id/{order_id}', response_model=int)
def delete_order_by_order_id(order_id: int, repo: OrderRepository = Depends(get_order_repo)):
    result = repo.delete_order_by_order_id(order_id)
    if type(result) is str:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=result)
    if result:
        return status.HTTP_200_OK
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No order with order_id={order_id} found.')
