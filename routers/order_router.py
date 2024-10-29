from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_session
from database.models import Order
from schemas.order_schemas import OrderCreate, OrderReturn

order_router = APIRouter()


@order_router.get('/get_orders')
def get_orders(session: Session = Depends(get_session)):
    result = session.execute(select(Order)).all()
    out = list()
    for item in result:
        item = item[0]
        out.append(OrderReturn(
            id=item.id,
            creation_date=item.creation_date,
            user_id=item.user_id,
            car_id=item.car_id
        ))
    return out


@order_router.get('/get_orders_user/{user_id}')
def get_orders_by_user_id(user_id: int):
    pass


@order_router.post('/add_order')
def add_order(order_data: OrderCreate, session: Session = Depends(get_session)):
    new_order = Order(user_id=order_data.user_id, car_id=order_data.car_id)
    session.add(new_order)
    session.commit()

    return OrderReturn(
        id=new_order.id,
        creation_date=new_order.creation_date,
        user_id=new_order.user_id,
        car_id=new_order.car_id
    )


@order_router.patch('/edit_order/{order_id}')
def edit_order(order_id: int, new_data):
    pass


@order_router.delete('/delete_order/{order_id}')
def delete_order(order_id: int):
    pass
