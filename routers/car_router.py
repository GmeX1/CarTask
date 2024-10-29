from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_session
from database.models import Car
from schemas.car_schemas import CarCreate, CarReturn

car_router = APIRouter()


@car_router.get('/get_cars')
def get_cars(session: Session = Depends(get_session)):
    result = session.execute(select(Car)).all()
    out = list()
    for item in result:
        item = item[0]
        out.append(CarReturn(
            id=item.id,
            name=item.name,
            brand=item.brand,
            price=item.price,
            engine_type=item.engine_type.name
        ))
    return out


@car_router.get('/get_car/{car_id}')
def get_car(car_id: int):
    pass


@car_router.post('/add_car')
def add_car(car_data: CarCreate, session: Session = Depends(get_session)):
    new_car = Car(name=car_data.name, brand=car_data.brand, price=car_data.price, engine_type=car_data.engine_type)
    session.add(new_car)
    session.commit()

    return CarReturn(
        id=new_car.id,
        name=new_car.name,
        brand=new_car.brand,
        price=new_car.price,
        engine_type=new_car.engine_type.name
    )


@car_router.patch('/edit_car/{car_id}')
def edit_car(car_id: int, new_data):
    pass


@car_router.delete('/delete_car/{car_id}')
def delete_car(car_id: int):
    pass
