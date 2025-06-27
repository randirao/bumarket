
from data import con, cur

def get_user_by_credentials(user):
    cur.execute(f"SELECT user_id, username, name, is_admin, created_at FROM users WHERE username = '{user['username']}' AND password = '{user['password']}'")
    result = cur.fetchone()
    if result:
        return result
    else:
        return None

def make_seller(seller):
    query = f"INSERT INTO users (username, password, name) VALUES ('{seller['username']}', '{seller['password']}', '{seller['name']}')"
    cur.execute(query)
    con.commit()
    return get_user_by_credentials(seller)


def get_all_sellers():
    query = f"SELECT username, name FROM users WHERE is_admin = 0"
    cur.execute(query)
    result = cur.fetchall()
    if result:
        return result
    return None


def find_by_username(username):
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cur.execute(query)
    result = cur.fetchone()
    if result:
        return result
    return None