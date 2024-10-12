from fastapi import APIRouter

order_router = APIRouter()


@order_router.get('/get_orders')
def get_orders():
    pass


@order_router.get('/get_orders_user/{user_id}')
def get_orders_by_user_id(user_id: int):
    pass


@order_router.post('/add_order')
def add_order():
    pass


@order_router.patch('/edit_order/{order_id}')
def edit_order(order_id: int, new_data):
    pass


@order_router.delete('/delete_order/{order_id}')
def delete_order(order_id: int):
    pass
