from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from database import get_session
from database.repositories import CarRepository
from schemas.car_schemas import CarCreate, CarReturn, CarEdit

car_router = APIRouter(prefix='/car')


def get_car_repo(session: Session = Depends(get_session)):
    return CarRepository(session)


@car_router.get('/get_cars', response_model=List[CarReturn])
def get_cars(repo: CarRepository = Depends(get_car_repo)):
    result = repo.get_cars()
    out = list()
    for item in result:
        out.append(CarReturn(
            id=item.id,
            name=item.name,
            brand=item.brand,
            price=item.price,
            engine_type=item.engine_type.name
        ))
    return out


@car_router.get('/get_car/{car_id}', response_model=CarReturn)
def get_car_by_id(car_id: int, repo: CarRepository = Depends(get_car_repo)):
    result = repo.get_car_by_id(car_id)
    if result:
        return CarReturn(
            id=result.id,
            name=result.name,
            brand=result.brand,
            price=result.price,
            engine_type=result.engine_type.name
        )
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No car with id={car_id} found.')


@car_router.post('/add_car', response_model=CarReturn)
def add_car(car_data: CarCreate, repo: CarRepository = Depends(get_car_repo)):
    result = repo.create_car(car_data)
    return CarReturn(
        id=result.id,
        name=result.name,
        brand=result.brand,
        price=result.price,
        engine_type=result.engine_type.name
    )


@car_router.patch('/edit_car/{car_id}', response_model=CarReturn)
def edit_car(car_id: int, new_data: CarEdit, repo: CarRepository = Depends(get_car_repo)):
    result = repo.edit_car_by_id(car_id, new_data)
    return CarReturn(
        id=result.id,
        name=result.name,
        brand=result.brand,
        price=result.price,
        engine_type=result.engine_type.name
    )


@car_router.delete('/delete_car/{car_id}', response_model=CarReturn)
def delete_car(car_id: int, repo: CarRepository = Depends(get_car_repo)):
    result = repo.delete_car_by_id(car_id)
    if result:
        return status.HTTP_200_OK
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No car with id={car_id} found.')
