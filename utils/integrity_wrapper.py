from psycopg2.errors import ForeignKeyViolation
from sqlalchemy.exc import IntegrityError


def check_fk_integrity(func):
    def wrapper_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IntegrityError as ex:
            if type(ex.orig) is ForeignKeyViolation:
                return ex.orig.pgerror
            return ex

    return wrapper_func
