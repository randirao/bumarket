from sqlite3 import Connection, Cursor
from typing import Optional

con: Optional[Connection] = None
cur: Optional[Cursor] = None

def get_connection(pymysql=None):
    return pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="todos",
        db="bumaket",
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor
    )
con = get_connection()
cur = con.cursor()