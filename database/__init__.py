from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER
from .models import Base, Car, Order, User

engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
session_maker = sessionmaker(bind=engine)


def get_session() -> Session:
    with session_maker() as session:
        yield session
