from fastapi import APIRouter

car_router = APIRouter()


@car_router.get('/get_cars')
def get_cars():
    pass


@car_router.get('/get_car/{car_id}')
def get_car(car_id: int):
    pass


@car_router.post('/add_car')
def add_car():
    pass


@car_router.patch('/edit_car/{car_id}')
def edit_car(car_id: int, new_data):
    pass


@car_router.delete('/delete_car/{car_id}')
def delete_car(car_id: int):
    pass
