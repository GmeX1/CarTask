from sqlalchemy import select, delete
from sqlalchemy.orm import Session

from database import Car
from schemas.car_schemas import CarCreate, CarEdit
from utils.integrity_wrapper import check_fk_integrity


class CarRepository:
    def __init__(self, session: Session):
        self.db = session

    def get_cars(self):
        result = self.db.execute(select(Car)).scalars().all()
        return result

    def get_car_by_id(self, car_id: int):
        result = self.db.execute(select(Car).where(Car.id == car_id)).scalars().one_or_none()
        return result

    def create_car(self, car_data: CarCreate):
        new_car = Car(name=car_data.name, brand=car_data.brand, price=car_data.price, engine_type=car_data.engine_type)
        self.db.add(new_car)
        self.db.commit()

        return new_car

    def edit_car_by_id(self, car_id: int, data: CarEdit):
        car = self.get_car_by_id(car_id)
        if car is None:
            return None

        for var, value in vars(data).items():
            setattr(car, var, value) if value else None
        self.db.commit()
        return car

    @check_fk_integrity
    def delete_car_by_id(self, car_id: int):
        car = self.get_car_by_id(car_id)
        if car is None:
            return None

        self.db.execute(delete(Car).where(Car.id == car_id))
        self.db.commit()
        return True
