from sqlalchemy import select, delete
from sqlalchemy.orm import Session

from database import User
from schemas.user_schemas import UserEdit, UserCreate
from utils.integrity_wrapper import check_fk_integrity


class UserRepository:
    def __init__(self, session: Session):
        self.db = session

    def get_users(self):
        result = self.db.execute(select(User)).scalars().all()
        return result

    def get_user_by_id(self, user_id: int):
        result = self.db.execute(select(User).where(User.id == user_id)).scalars().one_or_none()
        return result

    def create_user(self, data: UserCreate):
        new_user = User(name=data.name)
        self.db.add(new_user)
        self.db.commit()
        return new_user

    def update_user_by_id(self, user_id: int, data: UserEdit):
        user = self.get_user_by_id(user_id)
        if user is None:
            return None

        for var, value in vars(data).items():
            setattr(user, var, value) if value else None
        self.db.commit()
        return user

    @check_fk_integrity
    def delete_user_by_id(self, user_id: int):
        user = self.get_user_by_id(user_id)
        if user is None:
            return None

        self.db.execute(delete(User).where(User.id == user_id))
        self.db.commit()
        return True
