from sqlalchemy import select, delete
from sqlalchemy.orm import Session

from database import Order
from schemas.order_schemas import OrderCreate, OrderEdit
from utils.integrity_wrapper import check_fk_integrity


class OrderRepository:
    def __init__(self, session: Session):
        self.db = session

    def get_orders(self):
        result = self.db.execute(select(Order)).scalars().all()
        return result

    def get_order_by_order_id(self, order_id: int):
        result = self.db.execute(select(Order).where(Order.id == order_id)).scalars().one_or_none()
        return result

    def get_orders_by_user_id(self, user_id: int):
        result = self.db.execute(select(Order).where(Order.user_id == user_id)).scalars().all()
        return result

    @check_fk_integrity
    def create_order(self, order_data: OrderCreate):
        new_order = Order(user_id=order_data.user_id, car_id=order_data.car_id)
        self.db.add(new_order)
        self.db.commit()
        return new_order

    @check_fk_integrity
    def edit_order_by_order_id(self, order_id: int, data: OrderEdit):
        order = self.get_order_by_order_id(order_id)
        if order is None:
            return None

        for var, value in vars(data).items():
            setattr(order, var, value) if value else None
        self.db.commit()
        return order

    def delete_orders_by_user_id(self, user_id: int):
        order = self.get_orders_by_user_id(user_id)
        if order is None:
            return None

        self.db.execute(delete(Order).where(Order.user_id == user_id))
        self.db.commit()
        return True

    def delete_order_by_order_id(self, order_id: int):
        order = self.get_order_by_order_id(order_id)
        if order is None:
            return None

        self.db.execute(delete(Order).where(Order.id == order_id))
        self.db.commit()
        return True
