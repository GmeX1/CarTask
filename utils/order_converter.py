from database import Order
from schemas.order_schemas import OrderReturn


def convert_orders(orders: list[Order] or Order or None):
    if orders is None:
        return None

    if type(orders) is not list:
        orders = [orders]
    out = [
        OrderReturn(
            id=order.id,
            creation_date=order.creation_date,
            user_id=order.user_id,
            car_id=order.car_id
        ) for order in orders
    ]
    return out
