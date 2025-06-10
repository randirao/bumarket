from error import UserNotFoundException
from . import cur
from . import con

def find_all():
    query = "select username, name, created_at from users where is_admin = 0"
    cur.execute(query)
    result = cur.fetchall()
    if result is None:
        raise UserNotFoundException()
    return result
